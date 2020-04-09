from sqlalchemy.sql import func
from settings import db


class NewsletterSubscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    confirmed = db.Column(db.Boolean, nullable=True)
    modified_at = db.Column(db.DateTime(timezone=True), default=func.now())
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return '<NewsletterSubscription id: {} email: {} confirmed: {}>'.format(
            self.id, self.email, self.confirmed
        )


# Must be called at after all our models are declared
db.create_all()
