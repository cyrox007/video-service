from sqlalchemy import Column, Integer, String, DATE, ForeignKey
from sqlalchemy.orm import Session

from setting import Config
from database import Database

from werkzeug.security import generate_password_hash, check_password_hash


class User(Database.Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False, unique=True)
    nickname = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    user_role = Column(Integer, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    avatar = Column(String(50), nullable=False)

    def __repr__(self):
        return f"User {self.id}"

    @classmethod
    def get_user(cls, db_session: Session, login):
        return db_session.query(User).filter(
            User.nickname == login
        ).first()

    @classmethod
    def check_user_by_email(cls, db_session: Session, email):
        return db_session.query(User).filter(
            User.email == email
        ).first()

    @classmethod
    def check_user_by_nickname(cls, db_session: Session, nickname):
        return db_session.query(User).filter(
            User.nickname == nickname
        ).first()

    @classmethod
    def insert_new_user(cls, db_session: Session, data: dict):
        new_user = User(
            email = data['email'],
            first_name = data['first-name'],
            last_name = data['last-name'],
            nickname = data['nickname'],
            password = generate_password_hash(data['password']),
            avatar = data['avatar'],
            user_role = Config.role['user']
        )
        try:
            db_session.add(new_user)
            db_session.commit()
            return True
        except Exception as e:
            print(e)
            return False