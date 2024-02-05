from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from website import db


class User(db.Model):
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
    posts = db.relationship("BlogPost", backref="author", lazy=True)


class BlogPost(db.Model):
    pass
