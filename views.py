from flask import abort, request, url_for, make_response
from flask.views import View
from sqlalchemy.sql import exists, expression

from settings import db
from models import NewsletterSubscription
from utils import is_email_valid


class NewsletterSubscriptionCreateView(View):
	methods = ['POST']

	def _get_validated_data(self, data):
		if 'email' not in data:
			abort(400, 'Field email is missing in your request')

		if not is_email_valid(data['email']):
			abort(400, 'Provided email has incorrect format')

		if db.session.query(NewsletterSubscription.query.filter_by(email=data['email']).exists()).scalar():
			abort(403, 'Provided email has been already subscribed')

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
			abort(403, 'Subscription does not exist or has been already confirmed')

		return {'msg': 'Newsletter subscription confirmed'}


class NewsletterSubscriptionDeleteView(View):
	methods = ['GET', 'DELETE']

	def dispatch_request(self, slug):

		deleted_count = NewsletterSubscription.query.filter_by(slug=slug).delete()
		db.session.commit()
		
		if deleted_count == 0:
			abort(403, 'Subscription does not exist or has been already deleted')

		return {'msg': 'Newsletter subscription deleted'}
