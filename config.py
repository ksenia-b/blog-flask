class Configuration(object):
    DEBUG = True
    SQL_ALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://admin:admin@localhost/test1'
    SECRET_KEY = 'DLFNOSFHNKDFHKSSAIOH'

    #flask security
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'


