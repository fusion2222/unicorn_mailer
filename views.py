from flask import request, url_for, jsonify
from flask.views import View
from sqlalchemy.sql import exists, expression

from settings import db
from models import NewsletterSubscription
from utils import is_email_valid, json_abort


class NewsletterSubscriptionCreateView(View):
	methods = ['POST']

	def _get_validated_data(self, data):
		if 'email' not in data:
			json_abort('Field email is missing in your request', 400)

		if not is_email_valid(data['email']):
			json_abort('Provided email has incorrect format', 400)

		if db.session.query(NewsletterSubscription.query.filter_by(email=data['email']).exists()).scalar():
			json_abort('Provided email has been already subscribed', 403)

		return data

	def dispatch_request(self):
		data = self._get_validated_data(request.form)

		ns = NewsletterSubscription(email=data['email'])
		db.session.add(ns)
		db.session.commit()

		return {
			'subscription_slug': ns.slug,
			'confirmation_link': url_for('newsletter_subscription__confirm', slug=ns.slug),
			'deletion_link': url_for('newsletter_subscription__delete', slug=ns.slug)
		}, 201


class NewsletterSubscriptionConfirmationView(View):
	methods = ['GET']

	def dispatch_request(self, slug):
		updated_count = NewsletterSubscription.query.filter_by(slug=slug).filter(
			NewsletterSubscription.confirmed != True
		).update({'confirmed': True})
		
		db.session.commit()

		if updated_count == 0:
			json_abort('Subscription does not exist or has been already confirmed', 403)

		return {'message': 'Newsletter subscription confirmed'}


class NewsletterSubscriptionDeleteView(View):
	methods = ['GET', 'DELETE']

	def dispatch_request(self, slug):

		deleted_count = NewsletterSubscription.query.filter_by(slug=slug).delete()
		db.session.commit()
		
		if deleted_count == 0:
			json_abort('Subscription does not exist or has been already deleted', 403)

		return {'message': 'Newsletter subscription deleted'}
