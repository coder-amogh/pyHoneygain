# HoneyGain API

A Python binding to interact with HoneyGain Dashboard API.

## Installation

```BASH
pip install pyHoneygain
```

## Usage

---

### Login with username and password:

```PYTHON
from pyHoneygain import HoneyGain

# Your HoneyGain (HG) login username and password
USERNAME = ""
PASSWORD = ""

# Initialise the HoneyGain object
user = HoneyGain()

# Optionally, when instantiating you can pass in the following attributes to the HoneyGain class:
```

| Attribute      | Description        | Default Value                   |
|----------------|--------------------|---------------------------------|
| API_PREFIX_URL | The API Prefix URL | /api                            |
| API_VERSION    | The API Version    | /v1                             |
| API_DOMAIN     | The API Domain     | https://dashboard.honeygain.com |

```PYTHON
# Call the login method
user.login(USERNAME, PASSWORD)
```

---

### Login with access token (JWT token):

```PYTHON
from pyHoneygain import HoneyGain

# Your HG's JWT Token
JWT_TOKEN = "eyeiufhuegjdvniu85yhjdfseu487y5urhjdfkseiwu89347yrjfdskiu8y4rjk"

# Initialise the HoneyGain object
user = HoneyGain()

# Call the login method
user.set_jwt_token(JWT_TOKEN)
```

---

### Add proxies for future requests:

```PYTHON
from pyHoneygain import HoneyGain

# With authentication
user.set_proxy("ip:port:username:password")

# Without authentication
user.set_proxy("ip:port")
```

## Functions

---

1. Get user info

    ```PYTHON
    user.me()
    ```
---

2. Get devices info

    ```PYTHON
    user.devices()
    ```

##### **Note: The /v1 and /v2 endpoint return different information as of 16th Feb 2022.**

---

3. Get stats

    ```PYTHON
    # Returns 30 days stats (earnings/credits info).
    user.stats()
    ```
---

4. Get JumpTask (JT) stats

    ```PYTHON
    # Returns 30 days JT stats (earnings/credits info).
    user.stats()
    ```
---

5. Get today's stats

    ```PYTHON
    # Returns today's earnings/credits info..
    user.stats_today()
    ```
---

6. Get today's JT stats

    ```PYTHON
    # Returns today's JT earnings/credits info..
    user.stats_today_jt()
    ```
---

7. Get notifications

    ```PYTHON
    # Returns notifications (if any)
    user.notifications()
    ```
---

8. Get payouts

    ```PYTHON
    # Returns pending payouts as per shown as dashboard
    user.payouts()
    ```

---

9. Request payout for BTC

    ```PYTHON
    # Requests payout, method as BTC to a BTC wallet address.
    BTC_ADDRESS = "bc1qr7twnwulkhd6gqwmkesvj5825kyz9mggy3mvcz"

    try:
        user.payout_to_btc(BTC_ADDRESS)
    except UserConfirmationRequiredError:
        # Sometimes HG will ask for user confirmation before accepting the payout request. 
        # So check your email and use the `add_user_confirmation` method on the user object to authenticate the user. 
        # Then you can call the payout_to_btc method again. 
        code = input("Enter the code: ")

        if user.add_user_confirmation(code):
            result = user.payout_to_btc(BTC_WALLET_ADDRESS)

            print("Withdrawal successful:", result)
    ```
---

10. Add user verification code

    ```PYTHON
    # Adds a user verification code as per the email
    code = input("Enter the verification code: ")

    user.add_user_confirmation(code) # Returns a boolean
    ```
---

11. Remove a proxy

    ```PYTHON
    # Removes a proxy for future requests.
    user.remove_proxy()
    ```
---

12. Change password

    ```PYTHON
    # Changes the password for the logged in user.
    user.change_password("oldpassword", "newpassword")
    ```
---

13. Get balances

    ```PYTHON
    # Gets balances info
    user.balances()
    ```
---

14. Open Honeypot

    ```PYTHON
    # Attempts to open Honeypot
    user.open_honeypot()
    ```
---

## Exceptions

- The following exceptions are defined.
    Exception | Reason
    --- | ---
    `NotLoggedInError` | Raised when you try to access protected routes (devices, payouts, etc).
    `UserConfirmationRequiredError` | Raised when you call an endpoint which requires user authentication.

- Note on `UserConfirmationRequiredError`: In case you get an error, you should check your email, add a user confirmation by using the `add_user_confirmation` method and then try to use the original method again.

---

