from datetime import datetime

from json import dumps
from flask import flash, jsonify, redirect, render_template, request, url_for
from flask import make_response

from .app import app
from .forms import CommentForm
from .models import db


@app.route("/")
def index():
    """Display a form to create a comment."""
    comment_form = CommentForm()
    return render_template(
        'index.html',
        form=comment_form,
    )


@app.route("/comment/new", methods=["POST"])
def create_comment():
    """Create a new comment and store it in the database."""
    comment_form = CommentForm()
    # Validate form
    if not comment_form.validate_on_submit():
        return redirect(url_for('index'))
    # Create comment object
    new_comment = {
        "body": request.form['body'],
        "ip": request.headers.get('X-Forwarded-For', request.remote_addr),
        "created_at": str(datetime.now()),
    }
    # Save new_comment in db
    db.child("comments").push(new_comment)
    return redirect(url_for('show_comments'))


@app.route("/comments", methods=["GET"])
def show_comments():
    """Show existing comments."""
    all_comments = db.child("comments").get().val()
    return jsonify(all_comments)


def valid_login(username, password):
    """Returns True if logged in, False otherwise."""
    return False  # TODO


@app.route("/v1/new/user", methods=["POST"])
def add_user():
    data = request.get_json()
    if data is None:
        # TODO: handle error
        pass
    else:
        db.child("users").push(data)
    res = ("OK", 200)  # body, status
    return make_response(res)


@app.route("/v1/new/idea", methods=["POST"])
def add_idea():
    # TODO: make sure user is logged in here
    data = request.get_json()
    if data is None:
        # TODO: handle error case
        pass
    else:
        db.child("ideas").push(data)
    res = ("OK", 200)  # body, status
    return make_response(res)

# # **************************
#
# from flask import Flask, request
# from flask_firebase import FirebaseAuth
# from flask_login import LoginManager, UserMixin, login_user, logout_user
# from flask_sqlalchemy import SQLAlchemy
#
# db = SQLAlchemy(app)
# auth = FirebaseAuth(app)
# login_manager = LoginManager(app)
#
# app.register_blueprint(auth.blueprint, url_prefix='/auth')
#
#
# class Account(UserMixin, db.Model):
#
#     __tablename__ = 'accounts'
#
#     account_id = db.Column(db.Integer, primary_key=True)
#     firebase_user_id = db.Column(db.Text, unique=True)
#     email = db.Column(db.Text, unique=True, nullable=False)
#     email_verified = db.Column(db.Boolean, default=False, nullable=False)
#     name = db.Column(db.Text)
#     photo_url = db.Column(db.Text)
#
#
# @auth.production_loader
# def production_sign_in(token):
#     account = Account.query.filter_by(firebase_user_id=token['sub']).one_or_none()
#     if account is None:
#         account = Account(firebase_user_id=token['sub'])
#         db.session.add(account)
#     account.email = token['email']
#     account.email_verified = token['email_verified']
#     account.name = token.get('name')
#     account.photo_url = token.get('picture')
#     db.session.flush()
#     login_user(account)
#     db.session.commit()
#
#
# @app.development_loader
# def development_sign_in(email):
#     login_user(Account.query.filter_by(email=email).one())
#
#
# @auth.unloader
# def sign_out():
#     logout_user()
#
#
# @login_manager.user_loader
# def load_user(account_id):
#     return Account.query.get(account_id)
#
#
# @login_manager.unauthorized_handler
# def authentication_required():
#     return auth.url_for('widget', mode='select', next=request.url)
