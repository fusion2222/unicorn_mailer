import re


EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

def is_email_valid(email):
	return EMAIL_REGEX.match(email)
