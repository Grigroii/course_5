from flask import request, render_template
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema, User
from implemented import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class MoviesView(Resource):
    def get(self):
        all_users = user_service.get_all()
        result = UserSchema(many=True).dump(all_users)
        return result, 200

    def post(self):
        req_json = request.json
        user_service.create(req_json)
        return "", 201


@user_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid):
        return UserSchema().dump(user_service.get_one(uid)), 200

    def put(self, uid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        user_service.update(req_json)
        return "", 204

    def delete(self, uid):
        user_service.delete(uid)
        return "", 204


@user_ns.route('/password')
class UpdateUserPasswordViews(Resource):
    def put(self):
        data = request.json

        email = data.get("email", None)
        old_password = data.get("old_password", None)
        new_password = data.get("new_password", None)

        user = user_service.get_user_by_email(email)

        if user_service.compare_hash_passwords(user.password, old_password):
            user.password = user_service.generate_password(new_password)

            result = UserSchema().dump(user)
            user_service.update(result)
        return "", 201
