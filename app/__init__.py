from flask import Flask
from config import config_options
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
photos = UploadSet('photos', IMAGES)

def create_app(config_name):
    app = Flask(__name__)

    # create app configurations
    app.config.from_object(config_options[config_name])

    # configure UploadSet
    configure_uploads(app, photos)

    # initialize flask extensions
    db.init_app(app)
    # register Blueprints

    return app 

