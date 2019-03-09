import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    if os.name == 'nt':
        DB_PATH = os.path.join(basedir, 'app.db')
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DB_PATH
    else:
        DB_PATH = os.path.join('/conf', '.id.db')
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DB_PATH
    SQLALCHEMY_TRACK_MODIFICATIONS = False
