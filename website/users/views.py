from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from website import db
from website.models import BlogPost, User
from website.users.forms import LoginForm, RegistrationForm, UpdateUserForm
from website.users.picture_handler import add_profile_pic

users = Blueprint("users", __name__)


@users.route("/register", methods=["GET", "POST"])
def register():
    """Register User"""
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            username=form.username.data,
            password=form.password.data,
        )

        db.session.add(user)
        db.session.commit()
        flash("Thank you for registering!")
        return redirect(url_for("users.login"))

    return render_template("register.html", form=form)


@users.route("/login", methods=["GET", "POST"])
def login():
    """Login User"""
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash("Logged in successfully!")

            # If user visits a page, they will be prompted to login
            next = request.args.get("next")

            if next == None or not next[0] == "/":
                next = url_for("core.index")

            return redirect(next)

    return render_template("login.html", form=form)


@users.route("/logout")
def logout():
    """Logout User"""
    logout_user()
    return redirect(url_for("core.index"))


@users.route("/account", methods=["GET", "POST"])
@login_required
def account():
    """Show the account page of the user"""
    form = UpdateUserForm()
    if form.validate_on_submit():
        if form.picture.data:
            username = current_user.username
            picture = add_profile_pic(form.picture.data, username)
            current_user.profile_image = picture  # profile_image taken from models.user

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("User Account Updated!")
        return redirect(url_for("users.account"))

    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_image = url_for(
        "static", filename="profile_pics/" + current_user.profile_image
    )
    return render_template("account.html", profile_image=profile_image, form=form)
