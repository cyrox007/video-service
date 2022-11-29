from flask.views import MethodView
from flask import render_template, request

from components.auth.decorators import get_session
from components.users.model import User


class RegisterPage(MethodView):
    def get(self):
        return render_template("auth/register/index.html")

    @get_session
    def post(self, db_session: 'db_session' = None):
        data: dict = {
            'email': request.form.get('email'),
            'first-name': request.form.get('first-name'),
            'last-name': request.form.get('surname'),
            'nickname': request.form.get('nickname'),
            'password': request.form.get('password'),
            'avatar': request.files['file']
        }

        print(data)

        return render_template("auth/register/index.html")


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