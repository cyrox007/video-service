from flask.views import MethodView
from flask import render_template, request, flash, redirect, url_for, session

from components.auth.decorators import get_session, login_required
from components.auth.forms import RegisterForm, LoginForm
from components.users.model import User
from components.auth.avatar_upload import avatar_processing


class RegisterPage(MethodView):
    def get(self):
        form = RegisterForm()
        return render_template("auth/register/index.html", form=form)

    @get_session
    def post(self, db_session: 'db_session' = None):
        form = RegisterForm()
        if form.validate_on_submit():
            data: dict = {
                'email': request.form.get('useremail'),
                'first-name': request.form.get('firstname'),
                'last-name': request.form.get('surname'),
                'nickname': request.form.get('nickname'),
                'password': request.form.get('password'),
                'avatar': avatar_processing(request.files['avatar'])
            }
            if User.insert_new_user(db_session, data):
                session['login'] = data['nickname']
                return redirect(url_for('index'))
        else: 
            flash("При заполнении формы вы допустили ошибку")
            

        return render_template("auth/register/index.html", form=form)


class LoginPage(MethodView):
    def get(self):
        form = LoginForm()
        return render_template(
            'auth/login/index.html', 
            form=form
            )

    @get_session
    def post(self, db_session: 'db_session' = None):
        form = LoginForm()

        useremail = request.form.get('useremail')
        password = request.form.get('password')

        userdata = User.login_user(db_session, useremail, password)
        if userdata is None:
            flash('Неверный логин или пароль')
            return render_template('/auth/login/index.html', form=form)

        session['login'] = userdata.nickname
        return redirect(url_for('index'))


class LogoutFunc(MethodView):
    @login_required
    def get(self, login: 'login' = None):
        session.clear()
        return redirect(url_for('index'))





class ValidEmail(MethodView):
    @get_session    
    def post(self, db_session: 'db_session' = None):
        if User.check_user_by_email(db_session, request.json) is not None:
            return {"ok": False}
        
        return {"ok": True}


class ValidNickname(MethodView):
    @get_session    
    def post(self, db_session: 'db_session' = None):
        if User.check_user_by_nickname(db_session, request.json) is not None:
            return {"ok": False}
        
        return {"ok": True}