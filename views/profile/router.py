from views.profile import views
from flask import Flask

def install(app: Flask):
    app.add_url_rule(
        '/profile/<string:nickname>',
        view_func=views.ProfilePage.as_view('profile')
    )