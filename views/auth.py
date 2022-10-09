from flask import request
from flask_restx import Resource, Namespace

from implemented import auth_service, user_service

auth_ns = Namespace('auth')


@auth_ns.route('/login')
class AuthViews(Resource):
    def post(self):
        data = request.json

        email = data.get("email", None)
        password = data.get("password", None)

        if None in [email, password]:
            return "", 400

        tokens = auth_service.generate_tokens(email, password)

        return tokens, 201

    def put(self):
        data = request.json
        access_token = data.get("access_token")
        refresh_token = data.get("refresh_token")

        validated = auth_service.validate_tokens(access_token, refresh_token)
        if validated == 'Fail':
            return "Invalid tokens", 400

        tokens = auth_service.approve_refresh_token(refresh_token)

        return tokens, 201


@auth_ns.route('/register')
class RegisterViews(Resource):
    def post(self):
        data = request.json

        email = data.get("email", None)
        password = data.get("password", None)

        if None in [email, password]:
            return "", 400

        data['favorite_genre'] = 1 # Поставил по дефолту любимый жанр: комедия
        user_service.create(data) # Передаём все обязательные поля

        return "", 201
