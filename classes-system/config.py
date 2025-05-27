from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

db = SQLAlchemy()


ALUNOS_API_URL = os.environ.get('ALUNOS_API_URL', 'http://localhost:5003')  

def create_app():
    app = Flask(__name__)


    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.init_app(app)

   
    from controller.sala_controller import sala_bp
    from controller.horario_controller import horario_bp  

    app.register_blueprint(sala_bp)
    app.register_blueprint(horario_bp)  


    with app.app_context():
        db.create_all()

    return app
