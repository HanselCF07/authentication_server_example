from flask import Blueprint, jsonify
from flask.views import MethodView
from app.repository import protected_repository as ProtectedRepository

protected_bp = Blueprint("protected", __name__)

# Register the view with its prefix
protected_bp.add_url_rule( "/api/v1/authentication/protected/data", view_func=ProtectedRepository.Data.as_view("protectedData") )

