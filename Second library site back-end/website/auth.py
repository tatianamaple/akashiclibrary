from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Patron_account
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__, template_folder="templates")

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = Patron_account.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('views.home'))

    return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        full_name = request.form.get('fullName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = Patron_account.query.filter_by(email=email).first()
    
        new_user = Patron_account(email=email, password=generate_password_hash(password1, method='sha256'), full_name=full_name)
        db.session.add(new_user)
        db.session.commit()
        login_user(user, remember=True)
        return redirect(url_for('views.home'))
       
    return render_template("sign_up.html")

@auth.route('/user-page')
@login_required
def user_page():
    return render_template("user_page.html")