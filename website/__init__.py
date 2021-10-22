from flask import Flask
from pytube import YouTube
import os
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "huhuhuhuhuhuhuhu"
    from .route import route
    app.register_blueprint(route, url_prefix = '/')
    
    return app
