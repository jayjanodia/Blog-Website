import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from website.core.views import core
from website.error_pages.handlers import error_pages

app = Flask(__name__)
app.register_blueprint(core)
app.register_blueprint(error_pages)

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
######################
