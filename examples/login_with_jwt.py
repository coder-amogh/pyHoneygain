from pyHoneygain import HoneyGain

LONG_SECURE_JWT_TOKEN = "eyeiufhuegjdvniu85yhjdfseu487y5urhjdfkseiwu89347yrjfdskiu8y4rjk"

user = HoneyGain()

user.set_jwt_token(LONG_SECURE_JWT_TOKEN)

print(user)
print("Trying to get /me:")

me = user.me()

if me:
	print(me)

