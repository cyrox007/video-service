from flask.views import MethodView
from flask import render_template

class MainPage(MethodView):
    def get(self):
        return render_template("/main/index.html")