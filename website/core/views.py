from flask import Blueprint, render_template, request

core = Blueprint("core", __name__)


@core.route("/")
def index():
    return render_template("index.html")


@core.route("/info")
def info():
    """General information about the website"""
    return render_template("about.html")
