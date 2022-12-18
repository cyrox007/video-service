from flask.views import MethodView
from flask import render_template, session
from components.auth.decorators import get_session, login_required
from components.users.model import User


class MainPage(MethodView):
    @login_required
    @get_session
    def get(self, login: 'login' = None, db_session: 'db_session' = None):
        user_data = User.get_user(db_session, login)
        return render_template(
            "/main/index.html", 
            user=user_data
            )