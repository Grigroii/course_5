from flask import Flask
from flask_restx import Api

from config import Config
from dao.model.user import User
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
from views.users import user_ns
from views.auth import auth_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    app.api = api
    #create_data(app, db)


#def create_data(app, db):
    #with app.app_context():
        #db.create_all()

        #u1 = User(name="vasya", surname="Ketlin", password="my_little_pony", email="user3132@mail.ru", favorite_genre=2)
        #u2 = User(name="oleg", surname="Jogard", password="qwerty", email="user3123@mail.ru", favorite_genre=3)
        #u3 = User(name="oleg", surname="Korguj", password="P@ssw0rd", email="admin313132@mail.ru", favorite_genre=6)

        #with db.session.begin():
            #db.session.add_all([u1, u2, u3])


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
