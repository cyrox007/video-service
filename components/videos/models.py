from sqlalchemy import Column, Integer, String, DATE, ForeignKey, Text
from sqlalchemy.orm import Session
from datetime import date

from database import Database


class Videos(Database.Base):
    __tablename__ = 'videos'

    id = Column(Integer, primary_key=True)
    status = Column(Integer, nullable=False)
    video_cover = Column(String, nullable=True)
    video_name = Column(String, nullable=False)
    video_description = Column(Text, nullable=False)
    video_filepath = Column(String, nullable=False)
    date_published = Column(DATE, default=date.today())
    number_views = Column(Integer, default=0)
    number_likes = Column(Integer, default=0)
    number_dislikes = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"Video {self.id}"

    @classmethod
    def insert_new_video(self, db_session: Session, data: list):
        new_video = Videos(
            status = 0,
            video_name = data['name'],
            video_description = data['description'],
            video_filepath = data['filepath'],
            user_id = data['user_id']
        )
        try:
            db_session.add(new_video)
            db_session.commit()
        except Exception as e:
            print(e)