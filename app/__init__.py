from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Configure CORS for production
    if config_name == 'production':
        CORS(app, origins=[
            'https://dashing-horse-e44477.netlify.app',
            'https://*.netlify.app',
            'http://localhost:5173',  # For local development
            'http://localhost:3000'   # Alternative local port
        ])
    else:
        CORS(app)  # Allow all origins in development
    
    from .routes.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Add root route
    @app.route('/')
    def root():
        return {
            'message': 'Movie Ticket Booking System',
            'api_base': '/api',
            'status': 'running'
        }
    
    return app
