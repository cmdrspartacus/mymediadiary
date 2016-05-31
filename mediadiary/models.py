from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from mediadiary.database import Base

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    media = Column(String(70))
    score = Column(Integer)
    review = Column(String(400))
    date = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    def __init__(self, name=None, media=None, review=None, score=None, date=None):
        self.name = name
        self.media = media
        self.review = review
        self.score = score
        self.date = date

    def __repr__(self):
        return '<User {}>'.format(self.name)

