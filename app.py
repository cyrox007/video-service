from flask import Flask
from setting import Config


def create_app() -> Flask:
    # imports
    from views.main import router as main_router
    from views.auth import router as auth_router
    from views.profile import router as profile_router
    from views.videos import router as video_router
    
    app = Flask(__name__, static_folder="static")
    app.config.from_object(Config)
    
    # calling
    main_router.install(app)
    auth_router.install(app)
    profile_router.install(app)
    video_router.install(app)
    
    return app