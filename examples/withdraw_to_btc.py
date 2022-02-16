from pyHoneygain import HoneyGain, exceptions

user = HoneyGain()

# Going to ignore login part, since that's mandatory for most of the endpoints/functions
# ...
# Assume it's logged in...

# Replace it with your address
BTC_WALLET_ADDRESS = "bc1qr7twnwulkhd6gqwmkesvj5825kyz9mggy3mvcz"

try:
	user.payout_to_btc(BTC_WALLET_ADDRESS)
except exceptions.UserConfirmationRequiredError:
	# Sometimes HG asks for verification code which is sent on email
	code = input("Enter the code: ")

	if user.add_user_confirmation(code):
		result = user.payout_to_btc(BTC_WALLET_ADDRESS)

		print("Withdrawal successful:", result)

