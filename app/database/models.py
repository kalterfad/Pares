from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Identity
from sqlalchemy.orm import relationship
from app.core.database import Base, engine, metadata


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    is_active = Column(Boolean, default=False, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=True)
    user_id = relationship('ReviewUserLinks', backref='user_links')


class Reviews(Base):
    __tablename__ = 'review'

    id = Column(Integer, primary_key=True)
    user = Column(String, nullable=False)
    date_created = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    text = Column(String, nullable=False)
    website = Column(String, nullable=False)
    review_id = relationship('ReviewUserLinks', backref='review_links')


class ReviewUserLinks(Base):
    __tablename__ = 'review_user_link'

    id = Column(String, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    review_id = Column(Integer, ForeignKey('review.id'), nullable=False)


class DoubleGisReviewCount(Base):
    __tablename__ = 'double_gis_review_count'

    id = Column(Integer, primary_key=True)
    place_id = Column(String, nullable=False)
    reviews_count = Column(Integer, nullable=False)


class FlampReviewCount(Base):
    __tablename__ = 'flamp_review_count'

    id = Column(Integer, primary_key=True)
    place_id = Column(String, nullable=False)
    reviews_count = Column(Integer, nullable=False)


if __name__ == '__main__':
    Base.metadata.create_all(engine)