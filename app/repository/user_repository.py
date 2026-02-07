from flask import jsonify, make_response
from flask.views import MethodView
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies
from config import Config



class DefaultViewer(MethodView):
    def post(self):
        try:
            access_token = create_access_token(
                identity="default_viewer",
                additional_claims={"role": "viewer"}
            )

            response = make_response(jsonify({"message": "Default Viewer"}), 200)

            set_access_cookies(response, access_token)  # Guardar token en cookie
            return response
        except Exception as e:
            return jsonify(msg="Server error", error=str(e)), 500


def validate_user(username, password):
    # Aquí iría la consulta a BD
    if username == "Hansel" and password == "password":
        return {"username": username, "role": "admin"}
    return None


class Login(MethodView):
    def post(self):
        try:
            user = validate_user("Hansel", "password")
            if not user:
                return jsonify(msg="Invalid credentials"), 401

            access_token = create_access_token(
                identity=user["username"],
                additional_claims={"role": user["role"]}
            )

            response = make_response(jsonify({"message": "Login successful"}), 200)

            set_access_cookies(response, access_token)  # Guardar token en cookie
            return response
        except Exception as e:
            return jsonify(msg="Server error", error=str(e)), 500


class Logout(MethodView):
    def post(self):
        response = make_response(jsonify({"message": "Logout successful"}), 200)
        unset_jwt_cookies(response)
        return response

