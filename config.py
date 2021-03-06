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
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    '''
    child configuration class for production
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    '''
    child configuration class for development
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://gitu_m:sqlpass@localhost/blogger'

    DEBUG = True

class TestConfig(Config):
    '''
    child configuration class for tests
    '''
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}