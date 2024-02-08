import os

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from website.core.views import core
from website.error_pages.handlers import error_pages
from website.users.views import users

app = Flask(__name__)

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
db = SQLAlchemy(app)

# allows you to make changes within your database
Migrate(app, db)

#################
# LOGIN CONFIGS #
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login"  # we are going to register a blueprint for users and which will have a 'login' view

#################


app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
