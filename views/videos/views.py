from flask import render_template, request, session
from flask.views import MethodView

from components.auth.decorators import login_required, get_session
from components.users.model import User
from components.videos.handler import temporary_video_loading
from components.videos.tasks import video_processing
from components.videos.forms import VideoForm


class VideoUploadPage(MethodView):
    @login_required
    @get_session
    def get(self, login: 'login' = None, db_session: 'db_session' = None):
        user = User.get_user(db_session, login)
        form = VideoForm()
        return render_template(
            '/videos/upload/index.html',
            user=user,
            form=form
        )
    
    @get_session
    def post(self, db_session: 'db_session' = None):
        user = User.get_user(db_session, session.get('login'))
        file = request.files['myfile']
        filepath = temporary_video_loading(file)
        video_processing.delay(filepath)
        try:
            return {"ok": 'ok'}
        except Exception as e:
            print(e)