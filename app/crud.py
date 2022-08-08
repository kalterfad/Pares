from sqlalchemy.orm import Session

from app import models
from app.core.database import test
from app.schemas import UserBase, ReviewBase


def get_user_data(chat_id: int, db: Session = test()):
    return db.query(models.User).filter(models.User.id == chat_id)


def create_user(user: UserBase, db: Session = test()):
    new_user = models.User(
        id=user.id,
        username=user.username,
        is_active=user.is_active
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_review(review_id: int, db: Session = test()):
    return db.query(models.Reviews).filter(models.Reviews.id == review_id)


def add_new_review(review: ReviewBase, db: Session = test()):
    new_review = models.Reviews(
        user=review.user,
        date_created=review.date_created,
        rating=review.rating,
        text=review.text
    )
    db.add(new_review)
    db.commit()
    db.refresh(new_review)

    return new_review
