from functools import wraps
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt

# The definition of roles and their associated permissions is simulated; this is usually configured in a database.
ROLES_PERMISSIONS = {
    "admin": ["read", "write", "delete"],
    "editor": ["read", "write"],
    "viewer": ["read"]
}

# Decorator to check if the user has the required permission
def permission_required(permission):
    def decorator(fn):
        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):
            # Obtain JWT claims
            claims = get_jwt()
            # Get the user role from the claims
            role = claims.get("role")
            # Verify if the role has the required permission
            if not role or permission not in ROLES_PERMISSIONS.get(role, []):
                return jsonify(msg="Access denied"), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator