import requests
import time

from .exceptions import *

class HoneyGain:
	def __init__(self, API_PREFIX_URL: str = "/api", API_VERSION: str = "/v1", API_DOMAIN: str = "https://dashboard.honeygain.com") -> None:
		"""Initialise HoneyGain API Client. """
		self.API_VERSION = API_VERSION
		self.API_PREFIX_URL = API_PREFIX_URL
		self.API_DOMAIN = API_DOMAIN
		self.API_BASE_URL = f'{self.API_DOMAIN}{self.API_PREFIX_URL}{self.API_VERSION}'
		self.jwt = None
		self.user_id = None
		self.remove_proxy()

	def __make_request(self, req_type: str, endpoint: str, headers: dict = {}, *args, **kwargs):
		"""Helper function to make requests. """

		return requests.request(req_type, f'{self.API_BASE_URL}{endpoint}', proxies = self.proxy_conf, headers = {
			**headers, **({
				"Authorization": f"Bearer {self.jwt}",
			} if self.jwt is not None else {}),
		}, *args, **kwargs)

	def set_proxy(self, proxy_str: str = None) -> bool:
		"""Sets the proxy for future API requests. """
		proxy = proxy_str.split(":")

		if len(proxy) > 2:
			ip, port, username, password = proxy

			self.proxy_conf = {
				"http": f"socks5://{username}:{password}@{ip}:{port}",
				"https": f"socks5://{username}:{password}@{ip}:{port}",
			}
		else:
			ip, port = proxy

			self.proxy_conf = {
				"http": f"socks5://{ip}:{port}",
				"https": f"socks5://{ip}:{port}",
			}

		return True

	def remove_proxy(self) -> bool:
		"""Removes the proxy for future API requests. """
		self.proxy_conf = None
		return True

	def set_jwt_token(self, jwt_token: str) -> bool:
		"""Sets the JWT token for future API requests. """
		self.jwt = jwt_token
		return True

	def __set_user_id(self, user_id: str) -> bool:
		"""Sets user_id which is required for some endpoints. """
		self.user_id = user_id
		return True

	def login(self, email: str, password: str) -> bool:
		"""Logs into the system for interacting with the API. """

		r = self.__make_request("POST", "/users/tokens", json = {
			"email": email,
			"password": password,
		})

		token = r.json()["data"]["access_token"]

		return self.set_jwt_token(token) if r.ok else False

	def handle_not_logged_in(self):
		if self.jwt is None:
			raise NotLoggedInError

	def preset_user_id(self):
		if self.user_id is None:
			return self.me()

	def change_password(self, current_password, new_password):
		"""Changes password. """
		self.handle_not_logged_in()

		r = self.__make_request("PUT", "/users/passwords", json = {
			'current_password': current_password,
			'new_password': new_password,
		})

		return r.ok

	def me(self):
		"""Returns user data. """
		self.handle_not_logged_in()

		r = self.__make_request("GET", "/users/me")

		self.__set_user_id(r.json().get("data", {}).get("id", None))

		me_data = r.json().get("data", None)

		return me_data if r.ok else False

	def devices(self):
		"""Returns devices info. As of 16th Feb 2022, /v1 and /v2 both return different data."""
		self.handle_not_logged_in()

		r = self.__make_request("GET", "/devices")

		devices_data = r.json().get("data", None)

		return devices_data if r.ok else False

	def stats(self):
		"""Returns 30 days earnings/credits info. """
		self.handle_not_logged_in()

		r = self.__make_request("GET", "/earnings/stats")

		stats_data = r.json()

		return stats_data if r.ok else False

	def stats_jt(self):
		"""Returns 30 days earnings/credits (only JumpTask) info. """
		self.handle_not_logged_in()

		r = self.__make_request("GET", "/jt-earnings/stats")

		stats_jt_data = r.json()

		return stats_jt_data if r.ok else False

	def stats_today(self):
		"""Returns today's earnings/credits info. """
		self.handle_not_logged_in()

		r = self.__make_request("GET", "/earnings/today")

		stats_today_data = r.json()

		return stats_today_data if r.ok else False
	
	def stats_today_jt(self):
		"""Returns today's JT earnings/credits info. """
		self.handle_not_logged_in()

		r = self.__make_request("GET", "/jt-earnings/today")

		stats_today_jt_data = r.json()

		return stats_today_jt_data if r.ok else False
	
	def wallet_stats(self):
		"""Returns wallet stats. """
		self.handle_not_logged_in()

		r = self.__make_request("GET", "/earnings/wallet-stats")

		wallet_stats_data = r.json()

		return wallet_stats_data if r.ok else False

	def notifications(self):
		"""Returns notifications. """
		self.handle_not_logged_in()

		self.preset_user_id()

		r = self.__make_request("GET", f"/notifications?user_id={self.user_id}")

		notifications_data = r.json().get("data", None)

		return notifications_data if r.ok else False

	def balances(self):
		"""Returns balances info. """
		self.handle_not_logged_in()

		r = self.__make_request("GET", "/users/balances")

		notifications_data = r.json().get("data", {})

		return notifications_data if r.ok else False

	def payouts(self):
		"""Returns payouts info. """
		self.handle_not_logged_in()

		r = self.__make_request("GET", "/payouts")

		payouts_data = r.json().get("data", None)

		return payouts_data if r.ok else False

	def actions_start_claim_honeypot_process(self, campaign_id: str, notification_hash: str) -> bool:
		"""Starts the process to claim honeypot. """
		self.handle_not_logged_in()

		self.preset_user_id()

		r = self.__make_request("POST", f"/notifications/{notification_hash}/actions", json = {
			"campaign_id": campaign_id,
			"action": "triggered",
			"user_id": self.user_id,
		})

		return r.ok

	def actions_accept_honeypot(self):
		"""Accept the honeypot. """
		self.handle_not_logged_in()

		r = self.__make_request("POST", "/contest_winnings")

		honeypot_data = r.json().get("data", None)

		return honeypot_data if r.ok else False
	
	def actions_stop_honeypot_process(self, campaign_id: str, notification_hash: str) -> bool:
		"""Stops the process to claim honeypot. """
		self.handle_not_logged_in()

		self.preset_user_id()

		r = self.__make_request("POST", f"/notifications/{notification_hash}/actions", json = {
			"campaign_id": campaign_id,
			"action": "closed",
			"user_id": self.user_id,
		})

		return r.ok

	def payout_to_btc(self, payout_address: str):
		"""Withdraw the balance to a BTC address. """
		self.handle_not_logged_in()

		r = self.__make_request("POST", "/payouts", json = {
			"method": "btc",
			"options": {
				"wallet": payout_address,
			},
		})

		if r.status_code == 403 and r.json()["title"] == "user_confirmation_required":
			# Need user confirmation
			raise UserConfirmationRequiredError
		
		return True

	def add_user_confirmation(self, verification_code: str) -> bool:
		"""Adds the user confirmation. Used for withdrawal requests. """
		self.handle_not_logged_in()

		r = self.__make_request("PATCH", "/user_confirmations", json = {
			"code": verification_code,
		})

		return r.ok

	def open_honeypot(self, retry_count: int = 5, delay: int = 2):
		count = 0

		while count < retry_count:
			notifications = self.notifications()

			for notification in notifications:
				if notification["template"] == "lucky_pot":
					self.actions_start_claim_honeypot_process(campaign_id = notification["campaign_id"], notification_hash = notification["hash"])

					credits = self.actions_accept_honeypot()

					self.actions_stop_honeypot_process(campaign_id = notification["campaign_id"], notification_hash = notification["hash"])

					return {
						"success": True,
						"credits": credits,
					}
			
			time.sleep(delay)

			count += 1

		return {
			"success": False,
			"credits": None,
		}

	def __repr__(self):
		return f"<HoneyGain Object at: {hex(id(self))}>"
