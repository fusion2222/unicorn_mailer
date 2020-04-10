import re

from flask import abort, jsonify, make_response


EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")


def is_email_valid(email):
	return EMAIL_REGEX.match(email)


def json_abort(message='', status_code=400):
	abort(make_response(jsonify(message=message), status_code))
