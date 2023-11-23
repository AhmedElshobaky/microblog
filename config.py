import os
from dotenv import load_dotenv
from ssl import create_default_context

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #email configuration
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['admin@example.com']

    POSTS_PER_PAGE = 5 #post

    LANGUAGES = ['en', 'ar', 'es', 'fr', 'de']

    CONTEXT= create_default_context(cafile=os.environ.get('CAFILE'))
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    ELASTIC_NAME = os.environ.get('ELASTIC_NAME')
    ELASTIC_PASSWORD = os.environ.get('ELASTIC_PASSWORD')