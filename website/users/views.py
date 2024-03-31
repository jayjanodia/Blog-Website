from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from website.extensions import db
from website.models import BlogPost, User
from website.users.forms import LoginForm, RegistrationForm, UpdateUserForm
from website.users.picture_handler import add_profile_pic
from flask import abort

from sqlalchemy.exc import IntegrityError

users = Blueprint("users", __name__)


@users.route("/register", methods=["GET", "POST"])
def register():
    """Register User"""
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            user = User(
                email=form.email.data,
                username=form.username.data,
                password=form.password.data,
            )
            db.session.add(user)
            db.session.commit()
            flash("Thank you for registering!")
            return redirect(url_for("users.login"))
        except IntegrityError:
            db.session.rollback()
            flash("Username or email already exists. Please choose a different one.")
            return redirect(url_for("users.register"))
    return render_template("register.html", form=form)


@users.route("/login", methods=["GET", "POST"])
def login():
    """Login User"""
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            abort(403, description=None)
        if user.check_password(form.password.data):
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
            current_user.profile_img = picture  # profile_img taken from models.user

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("User Account Updated!")
        return redirect(url_for("users.account"))

    elif request.method == "GET":
        # user is not submitting anything, so just grab the username and email
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_img = url_for("static", filename="profile_pics/" + current_user.profile_img)
    return render_template("account.html", profile_img=profile_img, form=form)


@users.route("/<username>")
def user_posts(username):
    page = request.args.get("page", 1, type=int)
    user = User.query.filter_by(
        username=username
    ).first_or_404()  # In case the user decides to manually input <username>, and then input it incorrectly, return a 404 error
    # Grab all blog posts by the particular user and sort the posts by date in decreasing order
    # paginate allows us to have pages. Here we have 5 blog posts per page
    blog_posts = (
        BlogPost.query.filter_by(author=user)
        .order_by(BlogPost.date.desc())
        .paginate(page=page, per_page=5)
    )
    return render_template("user_blog_posts.html", blog_posts=blog_posts, user=user)
