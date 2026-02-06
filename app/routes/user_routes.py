from flask import Blueprint
from flask.views import MethodView
from app.repository import user_repository as UserRepository

user_bp = Blueprint("user", __name__)

# Registrar la vista con prefijo /api/user
#user_bp.add_url_rule( "/register", view_func=UserRepository.Register.as_view("register") )
#user_bp.add_url_rule( "/profile", view_func=UserRepository.Profile.as_view("profile") )
#user_bp.add_url_rule( "/default/viewer", view_func=UserRepository.DefaultViewer.as_view("defaultViewer") )

user_bp.add_url_rule( "/api/v1/authentication/user/login", view_func=UserRepository.Login.as_view("userLogin") )
user_bp.add_url_rule( "/api/v1/authentication/user/logout", view_func=UserRepository.Logout.as_view("userLogout") )

