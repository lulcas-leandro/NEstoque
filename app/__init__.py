from flask import Flask 
from app.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    @app.route('/main')
    def main_route():
        return "<h1> Fabrica de aplicação funcionando</h1>"
    
    return app