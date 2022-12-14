from views.auth import view
from flask import Flask

def install(app: Flask):
    app.add_url_rule(
        '/registration',
        view_func=view.RegisterPage.as_view('register')
    )
    app.add_url_rule(
        '/login',
        view_func=view.LoginPage.as_view('login')
    )
    app.add_url_rule(
        '/logout',
        view_func=view.LogoutFunc.as_view('logout')
    )
    app.add_url_rule(
        '/register/valid-email',
        view_func=view.ValidEmail.as_view('valid-email')
    )
    app.add_url_rule(
        '/register/valid-nickname',
        view_func=view.ValidNickname.as_view('valid-nickname')
    )