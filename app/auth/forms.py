from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, DataRequired, Length


class LoginForm(FlaskForm):

    email = StringField(
        label='Email',
        validators=[
            Email(),
            DataRequired()
        ]
    )

    password = PasswordField(
        label='Password',
        validators=[
            DataRequired()
        ]
    )


class SignupForm(FlaskForm):

    name = StringField(
        label='Name',
        validators=[
            DataRequired(),
            Length(max=15)
        ]
    )

    email = StringField(
        label='Email',
        validators=[
            Email(),
            DataRequired(),
            Length(max=50)
        ]
    )

    password = PasswordField(
        label='Password',
        validators=[
            DataRequired(),
            Length(min=8, max=80)
        ]
    )
