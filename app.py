from flask import Flask
from setting import Config


def create_app() -> Flask:
    # imports
    from views.main import router as main_router
    
    app = Flask(__name__, static_folder="static")
    app.config.from_object(Config)
    
    # calling
    main_router.install(app)
    
    return app