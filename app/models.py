from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base, engine, metadata


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    is_active = Column(Boolean, default=False, nullable=False)
    user_id = relationship('ReviewUserLinks', backref='user_links')


class Reviews(Base):
    __tablename__ = 'review'

    id = Column(Integer, primary_key=True)
    user = Column(String, nullable=False)
    date_created = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    text = Column(String, nullable=False)
    review_id = relationship('ReviewUserLinks', backref='review_links')


class ReviewUserLinks(Base):
    __tablename__ = 'review_user_link'

    id = Column(String, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    review_id = Column(Integer, ForeignKey('review.id'), nullable=False)

if __name__ == '__main__':
    Base.metadata.create_all(engine)