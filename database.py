from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from setting import Config

class Database:
    def connect_database():
        engine = create_engine(Config.database_link())
        db_session = Session(bind=engine)
        return db_session
    
    Base = declarative_base()