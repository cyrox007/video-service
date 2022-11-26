from flask import Flask


def create_app() -> Flask:
    # imports
    from views.main import router as main_router
    
    app = Flask(__name__, static_folder="static")
    
    # calling
    main_router.install(app)
    
    return app