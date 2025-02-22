import os
from flask import Flask
from config import config
from app.extensions import db, migrate, login_manager
environment_config = os.getenv('ENVIRONMENT_CONFIG') or 'development'
def create_app(config_class=environment_config):
    print(config_class)
    app = Flask(__name__)
    app.config.from_object(config[config_class])
    # Initialize Flask extensions here
    db.init_app(app)
    migrate.init_app(app,db)
    login_manager.init_app(app)
    # Register blueprints here
    # auth blueprint
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    # Memes blueprint
    from app.memes import bp as memes_bp
    app.register_blueprint(memes_bp, url_prefix='/memes')
    # Main blueprint
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    # Message blueprint
    from app.messages import bp as messages_bp
    app. register_blueprint(messages_bp,url_prefix='/messages')
    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'
    return app