import os

basedir = os.path.abspath(os.path.dirname(__file__))

print(basedir)

class Config: 
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLACHEMY_DATABASE_URI = os.environ.get('DATEBASE_URI')\
        or 'sqlite://' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
