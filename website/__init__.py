from flask import Flask
from website.core.views import core
from website.error_pages.handlers import error_pages

app = Flask(__name__)
app.register_blueprint(core)
app.register_blueprint(error_pages)
