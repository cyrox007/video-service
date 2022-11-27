from flask.views import MethodView
from flask import render_template
from components.auth.decorators import get_session
from components.users.model import User


class MainPage(MethodView):
    @get_session
    def get(self, db_session: 'db_session' = None):
        User.get_user(db_session)
        return render_template("/main/index.html")