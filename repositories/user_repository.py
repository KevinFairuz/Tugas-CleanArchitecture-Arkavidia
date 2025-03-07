from models.user import User
from database.db import db

class UserRepository:
  @staticmethod
  def get_users():
    return User.query.all()

  @staticmethod
  def add_user(user):
    db.session.add(user)
    db.session.commit()
