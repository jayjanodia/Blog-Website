from datetime import datetime, timezone

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from website.extensions import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    # string since it will be a link to the particular file the user uploads, image can't be nullable so we provide a default image
    profile_img = db.Column(
        db.String(64), nullable=False, default="default_profile.png"
    )
    # email and username have to be unique each time, users can't have the same email address and username
    # Indexing is used to speed up data retrieval from a table, at the cost of additional writes and the storage required to maintain it: https://www.postgresqltutorial.com/postgresql-indexes/postgresql-create-index/
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    # backref is an attribute call, here relationship between blogpost and user.
    # items should be loaded lazily when the property is first accessed, using a separate SELECT statement, or identity map fetch for simple many-to-one references.
    posts = db.relationship("BlogPost", backref="author", lazy=True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Username {self.username}"


class BlogPost(db.Model):
    users = db.relationship(User, overlaps="author,posts")
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), nullable=False
    )  # we are calling the users table class, and the id attribute from the table class
    date = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    title = db.Column(db.String(128), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return f"Post ID: {self.id} -- Date: {self.date} -- Title: {self.title}"
