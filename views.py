from flask import abort, request, url_for
from flask.views import View

from settings import db
from models import NewsletterSubscription
from utils import is_email_valid


class NewsletterSubscriptionCreateView(View):
	methods = ['POST']

	def dispatch_request(self):
		if 'email' not in request.form:
			abort(400, 'Field email is missing in your request')

		if not is_email_valid(request.form['email']):
			abort(400, 'Provided email has incorrect format')

		ns = NewsletterSubscription(email=request.form['email'])
		db.session.add(ns)
		db.session.commit()		

		return {
			'subscription_slug': ns.slug,
			'confirmation_link': url_for('newsletter_subscription__confirm', slug=ns.slug),
			'deletion_link': url_for('newsletter_subscription__delete', slug=ns.slug)
		}


class NewsletterSubscriptionConfirmationView(View):
	methods = ['GET']

	def dispatch_request(self, slug):

		# 	ns = NewsletterSubscription(email='admin@example.com')
		# 	db.session.add(ns)
		# 	db.session.commit()
		# 	# NewsletterSubscription.query.filter_by(username='admin').first()
		# 	# str(NewsletterSubscription.query.all())
		# 
		# 	return str(NewsletterSubscription.query.filter_by(email='admin@example.com').first())

		return 'Hello {}!'.format(slug)

class NewsletterSubscriptionDeleteView(View):
	methods = ['GET', 'DELETE']  # GET so it is easily accessible.

	def dispatch_request(self, slug):

		# 	ns = NewsletterSubscription(email='admin@example.com')
		# 	db.session.add(ns)
		# 	db.session.commit()
		# 	# NewsletterSubscription.query.filter_by(username='admin').first()
		# 	# str(NewsletterSubscription.query.all())
		# 
		# 	return str(NewsletterSubscription.query.filter_by(email='admin@example.com').first())

		return 'Hello {}!'.format(slug)