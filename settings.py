import json
import os

from sqlalchemy import create_engine


CONF = {}

# Load conf file
if not os.path.isfile('conf.json'):
	raise OSError('File conf.json not found')

with open('conf.json') as f:
	CONF.update(json.loads(f.read()))

DB_ENGINE = create_engine('sqlite:///db.sqlite3')
DB_CONNECTION = DB_ENGINE.connect()
