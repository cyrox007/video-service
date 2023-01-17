from flask import Flask
from views.videos import views

def install(app: Flask):
    app.add_url_rule(
        '/video/upload',
        view_func=views.VideoUploadPage.as_view('video-upload')
    )