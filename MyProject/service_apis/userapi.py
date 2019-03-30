from flask import current_app, jsonify, request
from flask_restful import Resource

from MyProject.service_apis_handler import user_handler


class UserApi(Resource):
    def get(self, username=None):
        if username:
            user_object = user_handler.get_user_by_username(username)
            return jsonify({"user": user_handler.get_user_json(user_object)})
        else:
            users = user_handler.get_user_by_filter()
            return jsonify({"users": [user_handler.get_user_json(user_object) for user_object in users]})

    def post(self):
        bodyparams = request.get_json()

        user_object = user_handler.create_user(bodyparams)

        return jsonify({"user": user_handler.get_user_json(user_object)})
