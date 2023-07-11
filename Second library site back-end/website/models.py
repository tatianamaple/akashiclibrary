from . import db
from flask_login import UserMixin

cart = db.Table('cart',
                db.Column('patron_account_id', db.Integer, db.ForeignKey('patron_account.id')),
                db.Column('book_id', db.Integer, db.ForeignKey('book.id'))
                )

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    authors_name = db.Column(db.String(150))
    genre = db.Column(db.String(150))
    publish_year = db.Column(db.String(150))
    publisher = db.Column(db.String(150))
    page_count = db.Column(db.Integer)
    image = db.Column(db.String(150))

class Patron_account(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    full_name = db.Column(db.String(150))
    downloaded_books = db.relationship('Book', secondary=cart, backref='patron_accounts')


