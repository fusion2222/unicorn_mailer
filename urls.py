from settings import app
from views import (
	NewsletterSubscriptionCreateView,
	NewsletterSubscriptionConfirmationView,
	NewsletterSubscriptionDeleteView
)


app.add_url_rule(
	'/newsletter-subscription',
	view_func=NewsletterSubscriptionCreateView.as_view(
		'newsletter_subscription__create'
	)
)
app.add_url_rule(
	'/newsletter-subscription/<slug>/confirm',
	view_func=NewsletterSubscriptionConfirmationView.as_view(
		'newsletter_subscription__confirm'
	)
)
app.add_url_rule(
	'/newsletter-subscription/<slug>',
	view_func=NewsletterSubscriptionDeleteView.as_view(
		'newsletter_subscription__delete'
	)
)
