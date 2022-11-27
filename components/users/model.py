from sqlalchemy import Column, Integer, String, DATE, ForeignKey
from sqlalchemy.orm import Session

from setting import Config
from database import Database


class User(Database.Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    user_role = Column(Integer, default=800, nullable=False)

    def __repr__(self):
        return f"User {self.id}"

    @classmethod
    def get_user(cls, db_session: Session):
        return db_session.query(User).all()