from flask import request

from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def get_by_username(self, username):
        user = self.session.query(User).filter(User.name == username).one_or_none()
        if not user:
            user = self.session.query(User).filter(User.email == username).one_or_none()
        return user

    def get_user_by_email(self, email):
        user = self.session.query(User).filter(User.email == email).one_or_none()
        return user

    def create(self, data):
        res = User(**data)
        self.session.add(res)
        self.session.commit()
        return res

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, data):
        user = self.get_one(data.get("id"))

        for k, v in data.items():
            setattr(user, k, v)


        self.session.add(user)
        self.session.commit()
