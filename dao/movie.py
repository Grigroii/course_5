
from dao.model.movie import Movie
from config import Config

class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Movie).get(bid)

    def get_all(self, filter, per_page=12):
        status = filter.get('status')
        page = filter.get('page')
        if page is not None:
            page = int(page)

        if status == 'new' and page is not None:
            return self.session.query(Movie).order_by(Movie.year.desc()).paginate(page, Config.ITEMS_PER_PAGE, max_per_page=Config.MAX_PAGE,
                                                                                  error_out=False).items
        elif status == 'new':
            return self.session.query(Movie).order_by(Movie.year.desc()).all()
        elif page is not None:
            return self.session.query(Movie).paginate(page, Config.ITEMS_PER_PAGE, max_per_page=Config.MAX_PAGE, error_out=False).items
        return self.session.query(Movie).all()

    def get_by_director_id(self, val):
        return self.session.query(Movie).filter(Movie.director_id == val).all()

    def get_by_genre_id(self, val):
        return self.session.query(Movie).filter(Movie.genre_id == val).all()

    def get_by_year(self, val):
        return self.session.query(Movie).filter(Movie.year == val).all()

    def create(self, movie_d):
        ent = Movie(**movie_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        movie = self.get_one(rid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, data):
        movie = self.get_one(data.get('id'))
        for k, v in data.items():
            setattr(movie, k, v)
        self.session.add(movie)
        self.session.commit()



