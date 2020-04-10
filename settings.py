import json
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


CONF = {}

# Load conf file
if not os.path.isfile('conf.json'):
	raise OSError('File conf.json not found')

with open('conf.json') as f:
	CONF.update(json.loads(f.read()))


app = Flask(__name__)

# Disables unused SQLAlchemy tracking for performance reasons
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)
