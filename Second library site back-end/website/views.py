from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .models import Book
from .models import Patron_account
from . import db

views = Blueprint('views', __name__, template_folder="templates")

@views.route('/')
@login_required
def home():
    return render_template("home.html")

@views.route('/books', methods=['GET','POST'])
@login_required
def books():
    if request.method == 'POST':
        new_book = Book(id=1, title='Moby-Dick, or The Whale', authors_name='Herman Melville', genre='Adventure Novel, Epic', publish_year='1851', publisher='Harper & Brothers', page_count=378, image='mobydick.jpg')
        new_book = Book(id=2, title='Paradise Lost', authors_name='John Milton', genre='Epic Poetry', publish_year='1667', publisher='Samuel Simmons', page_count=512, image='paradiselost.jpg')
        new_book = Book(id=3, title='Frankenstein; or, The Modern Prometheus', authors_name='Mary Shelley', genre='Gothic Novel, Science Fiction', publish_year='1818', publisher='Lackington, Hughes, Harding, Mavor & Jones', page_count=280, image='Frankenstein.jpg')
        new_book = Book(id=4, title='Hamlet', authors_name='William Shakespeare', genre='Shakespearean tragedy', publish_year='1603', publisher='Nicholas Ling & John Trundell', page_count=104, image='hamlet.jpg')
        new_book = Book(id=5, title='Anne of Green Gables', authors_name='Lucy Maud Montgomery', genre='Realism, Coming-of-Age', publish_year='1908', publisher='L.C. Page & Co', page_count=336, image='anneofgreengables.jpg')
        new_book = Book(id=6, title='The Marriage of Heaven and Hell', authors_name='William Blake', genre='Romanticism', publish_year='1790', publisher='William Blake', page_count=24, image='marriage.jpg')
        new_book = Book(id=7, title='Flowers for Algernon', authors_name='Daniel Keyes', genre='Science Fiction', publish_year='1966', publisher='Harcourt, Brace & World', page_count=311, image='flowersforalgernon.jpg')
        new_book = Book(id=8, title='Prometheus Unbound', authors_name='Percy Bysshe Shelley', genre='Lyrical Drama, Romanticism', publish_year='1820', publisher='C. and J. Ollier', page_count=100, image='prometheusunbound.jpg')
        new_book = Book(id=9, title='Crime and Punishment', authors_name='Fyodor Dostoevsky', genre='Realism, Psychological Novel', publish_year='1866', publisher='The Russian Messenger', page_count=576, image='cimeandpunishment.jpg')
        new_book = Book(id=10, title='The Catcher in the Rye', authors_name='J. D. Salinger', genre='Coming-of-Age', publish_year='1951', publisher='Little, Brown and Company', page_count=234, image='catcher.jpg')

        db.session.add(new_book)
        db.session.commit()
    books = Book.query.all()
    return render_template("books.html", books=books)






