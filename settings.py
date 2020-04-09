import json


CONF = {}

# Load conf file
if not os.path.isfile('conf.json'):
	raise OSError('File conf.json not found')

with open('conf.json') as f:
	CONF.update(json.loads(f.read()))


