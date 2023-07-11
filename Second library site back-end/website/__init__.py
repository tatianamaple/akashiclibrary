from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db=SQLAlchemy()
DB_NAME = "database.db"

def create_app(__name__):
    app = Flask(__name__, static_url_path='', static_folder='website/static', template_folder='website/templates')
    app.config['SECRET_KEY'] = 'i love bananas'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint (views, url_prefix='/')
    app.register_blueprint (auth, url_prefix='/')

    from .models import Patron_account, Book

    with app.app_context():
        db.create_all()
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Patron_account.query.get(int(id))

    return app
