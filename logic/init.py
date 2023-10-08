from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
    db.init_app(app)

    from .patientcontroller import bp as main_bp
    app.register_blueprint(main_bp)
    return app
