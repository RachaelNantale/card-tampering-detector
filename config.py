import os
from os import environ

class Config(object):
    
    DEBUG = False
    TESTING = False
    
    basedir    = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = 'scr3tK3y'
    DB_USERNAME = "root"
    DB_PASSWORD = "root"
    
    UPLOADS = "/Applications/MAMP/htdocs/udemy/data_science/pan_card_tampering/pan_card_flask/app/static/uploads"
    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None
    
class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = "pan-card"
    DB_USERNAME = "root"
    DB_PASSWORD = "root"

    UPLOADS = "/Applications/MAMP/htdocs/udemy/data_science/pan_card_tampering/card-tampering-detector/app/static/uploads"
    SESSION_COOKIE_SECURE = False
    
class TestingConfig(Config):
    DEBUG = True

    DB_NAME = "pan-card"
    DB_USERNAME = "root"
    DB_PASSWORD = "root"

    UPLOADS = "/Applications/MAMP/htdocs/udemy/data_science/pan_card_tampering/card-tampering-detector/app/static/uploads"
    URL = "/Applications/MAMP/htdocs/udemy/data_science/pan_card_tampering/card-tampering-detector/app/static/"
    

    SESSION_COOKIE_SECURE = False

 
class DebugConfig(Config):
    DEBUG = False

    
    
    