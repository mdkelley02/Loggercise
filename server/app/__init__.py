from flask import Flask
import os
from app.configs import DevelopmentConfig, ProductionConfig
from app.extensions.extensions import db, ma, cors
from app.static_data import insert_initial_data
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
config_map = {"development": DevelopmentConfig, "production": ProductionConfig}

def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)



def create_app():
    app = Flask(__name__)
    config = config_map.get(os.getenv("FLASK_ENV", "development"))
    app.config.from_object(config)
    
    register_extensions(app)

    from app.api import api_bp as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")

    with app.app_context():
        db.drop_all()
        db.create_all()

        # insert_initial_data(db)


    return app