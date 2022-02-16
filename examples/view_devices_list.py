from pyHoneygain import HoneyGain

user = HoneyGain()

# Going to ignore login part, since that's mandatory for most of the endpoints/functions
# ...
# Assume it's logged in...

for device in user.devices():
	print(f'Device with ID: {device["id"]} has total traffic of: {device["stats"]["total_traffic"]} bytes.')
