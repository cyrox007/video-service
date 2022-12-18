import functools
from flask import redirect, url_for, session
from database import Database


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        if session.get('login') is None:
            return redirect(url_for('login'))
        
        kwargs['login'] = session.get('login')
        return view(*args, **kwargs)

    return wrapped_view


def get_session(view):
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        kwargs['db_session'] = Database.connect_database()
        try:
            response = view(*args, **kwargs)
        finally:
            kwargs['db_session'].close()
        
        return response

    return wrapped_view