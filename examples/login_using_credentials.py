from pyHoneygain import HoneyGain

EMAIL, PASSWORD = ("email@example.com", "yourstrongpassword",)

user = HoneyGain()

if user.login(EMAIL, PASSWORD):
	print(user)
	print("Logged in!")
	print("JWT Token:", user.jwt)
