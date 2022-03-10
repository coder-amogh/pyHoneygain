from pyHoneygain import HoneyGain

LONG_SECURE_JWT_TOKEN = "eyeiufhuegjdvniu85yhjdfseu487y5urhjdfkseiwu89347yrjfdskiu8y4rjk"

user = HoneyGain()

user.set_jwt_token(LONG_SECURE_JWT_TOKEN)

print(user)

result = user.open_honeypot()

print("Worked:", result["success"])
print("Credits info:", result["credits"])

