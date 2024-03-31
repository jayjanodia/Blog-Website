from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import (  # allows users to upload png/jpeg to display profile picture
    FileAllowed,
    FileField,
)
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from website.models import User


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")


class RegistrationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            EqualTo("confirm_password", message="Passwords must match!"),
        ],
    )
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Register!")

    def check_email(self, field):
        """
        Confirm that the email inputted by the user has not been taken already
        """
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Your email has been registered already")

    def check_username(self, field):
        """
        Confirm that the username inputted by the user has not been taken already
        """
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Your username has been registered already")


class UpdateUserForm(FlaskForm):
    """
    allows the user to input their email, username or picture
    """

    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired()])
    picture = FileField(
        "Update profile picture",
        validators=[FileAllowed(["jpg", "png", "jpeg", "gif"])],
    )
    submit = SubmitField("Update")

    def check_email(self, field):
        """
        Confirm that the email inputted by the user has not been taken already
        """
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Your email has been registered already")

    def check_username(self, field):
        """
        Confirm that the username inputted by the user has not been taken already
        """
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Your username has been registered already")
