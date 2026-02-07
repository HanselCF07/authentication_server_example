from flask import jsonify
from flask.views import MethodView
from app.utils.rbac import permission_required


class Data(MethodView):
    # Example of using the permissions decorator
    @permission_required("read")
    def get(self):
        return jsonify({"msg": "Content protected from the repository"})

    # Example of using the permissions decorator
    @permission_required("write")
    def post(self):
        return jsonify({"msg": "Content protected edited"})

    # Example of using the permissions decorator
    @permission_required("delete")
    def delete(self):
        return jsonify({"msg": "Content protected deleted"})