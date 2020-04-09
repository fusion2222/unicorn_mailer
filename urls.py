from flask import Flask
from settings import app, db
from models import NewsletterSubscription


@app.route('/')
def hello_world():
	
	ns = NewsletterSubscription(slug='boris', email='admin@example.com')
	db.session.add(ns)
	db.session.commit()
	# NewsletterSubscription.query.filter_by(username='admin').first()
	
	return str(NewsletterSubscription.query.all())
