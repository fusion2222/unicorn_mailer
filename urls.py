from flask import Flask

from settings import app, db
from models import NewsletterSubscription


@app.route('/')
def hello_world():
	ns = NewsletterSubscription(email='admin@example.com')
	db.session.add(ns)
	db.session.commit()
	# NewsletterSubscription.query.filter_by(username='admin').first()
	# str(NewsletterSubscription.query.all())

	return str(NewsletterSubscription.query.filter_by(email='admin@example.com').first())
