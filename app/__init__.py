from flask import Flask, Blueprint, jsonify
from flask_jwt_extended import JWTManager
from config import Config

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    jwt.init_app(app)

    # Custom handler for missing or invalid tokens (unauthorized access)
    @jwt.unauthorized_loader
    def my_unauthorized_callback(err_str):
        return jsonify({
            'status': 401,
            'msg': 'Missing or invalid access. Please log in to access this resource.'
        }), 401

    # Blueprint raíz con prefijo /api
    api_bp = Blueprint("api", __name__)
    #api_bp = Blueprint("api", __name__, url_prefix="/api/v1/authentication") # Alternativa con prefijo global

    # Importar subrutas
    from app.routes.user_routes import user_bp
    from app.routes.protected_routes import protected_bp

    # Registrar sub-blueprints dentro del api_bp
    api_bp.register_blueprint(user_bp)
    api_bp.register_blueprint(protected_bp)

    # Registrar el blueprint raíz en la app
    app.register_blueprint(api_bp)


    return app
