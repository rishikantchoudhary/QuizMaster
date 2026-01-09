import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-for-local-testing'
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS') == 'true'

    uri = os.environ.get('SQLALCHEMY_DATABASE_URI')

    if uri and uri.startswith('sqlite:///'):
        db_name = uri.split('sqlite:///')[-1]
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, db_name)
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'db.sqlite3')