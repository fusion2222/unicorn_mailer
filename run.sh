#!/bin/bash

if [ ! -d ./.venv ]; then
	echo "[+] Setting up Virtualenv..."
    virtualenv .venv
fi

if [ ! -f ./conf.json ]; then
	cp ./conf.json.example ./conf.json
	echo "[+] Configure your local conf.json file and execute this script again."
	echo "[+] Exiting..."
	exit 1
fi

source ./.venv/bin/activate
pip install -r requirements.txt


if [ $1 = 'dev' ]; then
	export FLASK_ENV=development
else
	export FLASK_ENV=production
fi

export FLASK_APP=urls.py
flask run
