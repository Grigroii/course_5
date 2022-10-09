from marshmallow import Schema, fields

from setup_db import db


class Favorite_Genre(db.Model):
    __tablename__ = 'favorite_genre'
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), primary_key=True)


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()