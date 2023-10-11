from flask import Flask
from flask_cors import CORS
# from os import environ

from database import db
from routes import todo_bp
# from app import create_app
from config import Config

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    # Initialize the database instance
    db.init_app(app)

    # Enable CORS for all routes
    CORS(app)

    # Import and register your app's blueprints and routes here
    app.register_blueprint(todo_bp)

    with app.app_context():
        db.create_all()

    return app