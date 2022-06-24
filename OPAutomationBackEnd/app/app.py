from flask import Flask, redirect, url_for, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from apifairy import APIFairy
from dotenv import load_dotenv

from app.config import DevelopmentConfig

# from app.ma import ma
# from app.db import db

from marshmallow import ValidationError

from sqlalchemy.exc import IntegrityError


# migrate = Migrate(compare_type=True)
cors = CORS()
apifairy = APIFairy()
load_dotenv()

def create_app(config_class=DevelopmentConfig):    
    app = Flask(__name__)
    
    # Configure the app from config file
    app.config.from_object(config_class)

    # Initialize the db
    # db.init_app(app)

    # linking migrations to the app
    # migrate.init_app(app, db)

    # linking marshmallow to the
    # ma.init_app(app)

    # enable CORS
    CORS(app)

    # linking apifairy to the app (for documentation)
    apifairy.init_app(app)

    # register blueprints
    from app.resources.AcceptanceLetters import acceptance_letters
    from app.resources.WelcomeEmails import welcome_emails
    from app.resources.ComputerAccessDirections import computer_access_directions
    from app.resources.NewApplicationFiller import new_application_filler 


    app.register_blueprint(acceptance_letters)
    app.register_blueprint(new_application_filler)
    app.register_blueprint(welcome_emails)
    app.register_blueprint(computer_access_directions)

    
    @app.errorhandler(Exception)
    def handle_error(e):
        print(e)
        if isinstance(e, ValidationError):
            return jsonify({"error":e.messages}), 400

        elif isinstance(e, IntegrityError):
            errorInfo = e.orig.args
            return jsonify({"error": errorInfo[1]}), 400
        return jsonify(e.args), 500

    return app