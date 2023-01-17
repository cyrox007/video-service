from flask import render_template
from flask.views import MethodView

from components.auth.decorators import get_session, login_required
from components.users.model import User


class ProfilePage(MethodView):
    @login_required
    @get_session
    def get(self, login: 'login' = None, db_session: 'db_session' = None, nickname = None):
        user_data: dict = User.get_user(db_session, login)
        return render_template(
            '/profile/index.html',
            user=user_data
        )