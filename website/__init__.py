import os

from flask import Flask
from flask_migrate import Migrate

from website.extensions import db, login_manager
from website.core.views import core
from website.error_pages.handlers import error_pages
from website.blog_posts.views import blog_posts
from website.users.views import users

app = Flask(__name__)

app.config["SECRET_KEY"] = "mysecret"

######################
### DATABASE SETUP ###

# get the absolute path of the current file
# eg: /Users/jayjanodia/Blog-Website/website
basedir = os.path.abspath(os.path.dirname(__file__))
# generate a sqlite database within this absolute location
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "data.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# allows you to make changes within your database
Migrate(app, db)

# flask db init
# flask db migrate -m "first migration"
# flask db upgrade

#################
# LOGIN CONFIGS #

login_manager.init_app(app)
login_manager.login_view = "users.login"  # we are going to register a blueprint for users and which will have a 'login' view

#################


app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
app.register_blueprint(blog_posts)
