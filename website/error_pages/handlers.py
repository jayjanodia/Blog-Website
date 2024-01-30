from flask import Blueprint, render_template

error_pages = Blueprint("error_pages", __name__)


@error_pages.app_errorhandler(404)
def error_404(error):
    """Page not found error"""
    return render_template("error_pages/404.html"), 404


@error_pages.app_errorhandler(403)
def error_403(error):
    """
    Forbidden access
    eg. One user tries to access the account of another user
    """
    return render_template("error_pages/403.html"), 403
