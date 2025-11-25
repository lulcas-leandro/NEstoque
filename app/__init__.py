from flask import Flask 
from app.config import Config
from app.extensions import db, migrate
from flask_login import LoginManager
from app.utils import to_local_time

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Por favor, faça o login para acessar esta pagina.'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    
    @app.template_filter('to_local')
    def to_local_filter(utc_dt):
        return to_local_time(utc_dt, app.config['TIMEZONE'])
    
    from app.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.stock import stock_bp
    app.register_blueprint(stock_bp)
    
    return app