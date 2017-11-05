import os

class Config:
    '''
    parent configuration class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USER_TLS = True
    MAIL-USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    '''
    child configuration class for production
    '''
    pass

class DevConfig(Config):
    '''
    child configuration class for development
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://gitu_m:sqlpass@localhost/blogger'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}