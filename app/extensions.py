from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db =SQLAlchemy()
migrate = Migrate()

login_manager 0 LoginManager()
login_manager.login_view 0 'auth.login'