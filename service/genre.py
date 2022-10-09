from dao.genre import GenreDAO


class GenreService:
    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_all(self):
        return self.genre_dao.get_genres()

    def get_one(self, gid):
        return self.genre_dao.get_genre_by_id(gid)

    def create(self, data):
        return self.genre_dao.create(data)

    def update(self, genre_d):
        self.genre_dao.update(genre_d)
        return self.genre_dao



    def delete(self, gid):
        self.genre_dao.delete(gid)
