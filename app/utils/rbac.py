from functools import wraps
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt

ROLES_PERMISSIONS = {
    "admin": ["read", "write", "delete"],
    "editor": ["read", "write"],
    "viewer": ["read"]
}

def permission_required(permission):
    def decorator(fn):
        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            role = claims.get("role")
            if not role or permission not in ROLES_PERMISSIONS.get(role, []):
                return jsonify(msg="Acceso denegado"), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator