from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileRequired, FileAllowed

from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email


class RegisterForm(FlaskForm):
    useremail = EmailField(
        "Email",
        validators=[DataRequired(), Email()], 
        render_kw={
            "placeholder": "Введите электронную почту"
            })
    
    firstname = StringField(
        "Имя", 
        validators=[DataRequired()],
        render_kw={
            "placeholder": "Введите ваше имя"
        })

    surname = StringField(
        "Фамилия", 
        validators=[DataRequired()],
        render_kw={"placeholder": "Введите вашу фамилию"})

    nickname = StringField(
        'Ник', 
        validators=[DataRequired()],
        render_kw={"placeholder": "Выберите ник"})

    password = PasswordField(
        "Пароль", 
        validators=[DataRequired()], 
        render_kw={"placeholder": "Задайте пароль"})
    
    passRepeat = PasswordField(
        "Повторите пароль", 
        validators=[DataRequired()],
        render_kw={"placeholder": "Повторите заданный пароль"})

    avatar = FileField(
        validators=[
            FileRequired(),
            FileAllowed(
                ['png', 'jpg'],
                'Images only!'
            )
    ])

    submit = SubmitField("Зарегестрироваться")

    """ recaptcha = RecaptchaField() """


class LoginForm(FlaskForm):
    useremail = EmailField(
        "Email",
        validators=[DataRequired(), Email()],
        render_kw={
            "placeholder": "Введите электронную почту"
            })

    password = PasswordField(
        "Пароль", 
        validators=[DataRequired()], 
        render_kw={"placeholder": "Введите пароль"})

    submit = SubmitField("Войти")