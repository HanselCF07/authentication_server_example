import os
from flask import Flask, Blueprint, jsonify
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from config import app_config
from dotenv import load_dotenv


# Common configuration for all environments: Dev, QA y Production
def create_app():
    app = Flask(__name__)

    # Load environment variables from the .env file
    load_dotenv()

    # Initialize the JWT extension, which will handle the creation, verification, and management of JWT tokens in the Flask application.
    # This allows you to protect routes and resources using JWT token-based authentication.
    jwt = JWTManager()

    # Load the configuration from the Config class, which contains common configurations for all environments (Dev, QA y Production).
    # This includes secret keys, JWT configurations, SQLAlchemy options, and more.
    config_name = os.getenv('FLASK_ENV')
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('../config.py')

    # Initialize the JWT extension with the Flask application, allowing the app to use JWT functionalities for protecting routes and managing authentication tokens.
    jwt.init_app(app)

    # Custom handler for missing or invalid tokens (unauthorized access)
    @jwt.unauthorized_loader
    def my_unauthorized_callback(err_str):
        return jsonify({
            'status': 401,
            'msg': 'Missing or invalid access. Please log in to access this resource.'
        }), 401

    # Initialize the Marshmallow extension with the Flask application, which facilitates object serialization and deserialization, as well as data validation in the application.
    ma = Marshmallow(app)
    # Initialize the SQLAlchemy extension with the Flask application, which allows you to interact with databases using the SQLAlchemy ORM.
    db = SQLAlchemy(app)

    try:
        from gevent import monkey
        with app.app_context():
            # This line is necessary to avoid issues with the connection pool when using gevent for asynchronous tasks.
            # It ensures that each thread (or greenlet) gets its own connection from the pool, preventing conflicts and ensuring proper database interactions in an asynchronous environment.
            db.engine.pool._use_threadlocal = True
    except ImportError:
        pass

    # Enable CORS for all routes, allowing requests from any origin. This is useful for enabling cross-origin requests in web applications, especially when the frontend and backend are hosted on different domains.
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    # Blueprint root
    api_bp = Blueprint("api", __name__) 
    #api_bp = Blueprint("api", __name__, url_prefix="/api/v1/authentication") # Alternative with global prefix

    # Import subroutes to avoid circular imports
    from app.routes.user_routes import user_bp
    from app.routes.protected_routes import protected_bp

    # Register sub-blueprints within the api_bp
    api_bp.register_blueprint(user_bp)
    api_bp.register_blueprint(protected_bp)

    # Register the root blueprint in the app
    app.register_blueprint(api_bp)

    return app
