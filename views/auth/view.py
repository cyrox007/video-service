from flask.views import MethodView
from flask import render_template, request, flash

from components.auth.decorators import get_session
from components.auth.forms import RegisterForm
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
            print(data)
        else: 
            flash("При заполнении формы вы допустили ошибку")
            """ User.insert_new_user(db_session, data) """

        return render_template("auth/register/index.html", form=form)


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