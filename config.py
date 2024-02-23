import os
from sqlalchemy  import create_engine
class Config(object):
    SECRET_KEY='CLAVE_SECRETA'
    SESSION_COOKIE_SEGURE=False
class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:123456@localhost/idgs802'