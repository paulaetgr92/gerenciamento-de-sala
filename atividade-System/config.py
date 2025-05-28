from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///atividade.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Importação e registro dos blueprints
    from controller.atividade_controller import atividade_bp
    app.register_blueprint(atividade_bp)

    with app.app_context():
        db.create_all()

    return app
