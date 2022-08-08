from sqlalchemy.orm import Session

from app.core.database import test
from app.models import User, Reviews, ReviewUserLinks
from app.schemas import UserBase, ReviewBase, ReviewUserLinkBase


def get_user_data(chat_id: int, db: Session = test()) -> UserBase:
    return UserBase(**db.query(User).filter(User.id == chat_id).first().__dict__)


def get_all_users(db: Session = test()):
    user_list = []
    for i in db.query(User).all():
        user_list.append(UserBase(**i.__dict__))

    return user_list


def create_user(user: UserBase, db: Session = test()):
    new_user = User(
        id=user.id,
        username=user.username,
        is_active=user.is_active
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_review(review_id: int, db: Session = test()) -> ReviewBase:
    return ReviewBase(**db.query(Reviews).filter(Reviews.id == review_id).first().__dict__)


def add_new_review(review: ReviewBase, db: Session = test()):
    new_review = Reviews(
        user=review.user,
        date_created=review.date_created,
        rating=review.rating,
        text=review.text
    )
    db.add(new_review)
    db.commit()
    db.refresh(new_review)

    return new_review


def get_review_link(link_id: str, db: Session = test()) -> ReviewUserLinkBase:
    return ReviewUserLinkBase(**db.query(ReviewUserLinkBase).filter(ReviewUserLinks.id == link_id).first().__dict__)


def create_new_review_link(review_link: ReviewUserLinkBase, db: Session = test()):
    new_review_link = ReviewUserLinks(
        id=review_link.id,
        user_id=review_link.user_id,
        review_id=review_link.review_id
    )
    db.add(new_review_link)
    db.commit()
    db.refresh(new_review_link)

    return new_review_link


if __name__ == '__main__':
    pass
