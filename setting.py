import os


class Config:
    # main
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'blablabla'
    WTF_CSRF_SECRET_KEY = 'a random string'
    RECAPTCHA_PUBLIC_KEY = 'test'
    
    PATH_TO_DIR = os.path.dirname(os.path.abspath(__file__))

    # Database
    db_name = os.environ.get('DB_NAME', 'red')
    db_user = os.environ.get('DB_USER', 'postgres')
    db_password = os.environ.get('DB_PASSWORD', 'postgres')
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_port = os.environ.get('DB_PORT', 5432)

    def database_link():
        return f'postgresql://{Config.db_user}:{Config.db_password}@'\
               f'{Config.db_host}:{Config.db_port}/{Config.db_name}'

    # User role
    role: dict = {
        'admin': 900,
        'author': 800,
        'moderator': 700,
        'user': 100
    }
    
    # avatar
    AVATAR_DIR = 'uploads/us_avatars/'
    FULL_AVATAR_DIR = 'static/'+AVATAR_DIR