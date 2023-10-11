# from flask import Flask
# from flask_cors import CORS
# # from os import environ

# from database import db
# from routes import todo_bp
# # from app import create_app
from config import Config
from __init__ import create_app





app = create_app(Config)
# CORS(app, origins=['http://localhost:5000', 'http://127.0.0.1:5001'])

