from flask import jsonify
from flask.views import MethodView
from app.utils.rbac import permission_required


class Data(MethodView):
    @permission_required("read")
    def get(self):
        return jsonify({"msg": "Contenido desde el repositorio"})

    @permission_required("write")
    def post(self):
        return jsonify({"msg": "Contenido editado"})

    @permission_required("delete")
    def delete(self):
        return jsonify({"msg": "Contenido eliminado"})