import os

class Config:
    '''
    parent configuration class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

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