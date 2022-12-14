from sqlalchemy.orm import Session

from core.database import test
from database.models import User, Reviews, ReviewUserLinks, FlampReviewCount, DoubleGisReviewCount
from database.schemas import UserBase, ReviewBase, ReviewUserLinkBase, ReviewsCount


def get_all_users(db: Session = test()):
    user_list = []
    for i in db.query(User).all():
        user_list.append(UserBase(**i.__dict__))

    return user_list


def get_user_data(user: UserBase, db: Session = test()) -> UserBase:
    user_data = db.query(User).filter(User.id == user.id).first()
    if user_data is None:
        new_user = User(
            id=user.id,
            username=user.username,
            is_active=user.is_active
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
    else:
        return UserBase(**user_data.__dict__)


def update_user_data(chat_id: int, update_data: dict, db: Session = test()):
    db.query(User).filter(User.id == chat_id).update(
        update_data
    )

    db.commit()


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


def get_review(review_id: int, db: Session = test()):
    review = db.query(Reviews).filter(Reviews.id == review_id).first()
    if review is None:
        return ReviewBase()
    else:
        return ReviewBase(**review.__dict__)


def add_new_review(review: ReviewBase, db: Session = test()):
    new_review = Reviews(
        id=review.id,
        user=review.user,
        date_created=review.date_created,
        rating=review.rating,
        text=review.text,
        website=review.website
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


def get_reviews_count(model: str, place: ReviewsCount, db: Session = test()):
    db_model = {
        'flamp': FlampReviewCount,
        'doublegis': DoubleGisReviewCount
    }

    reviews_count = db.query(db_model[model]).filter(db_model[model].place_id == place.place_id).first()
    if reviews_count is None:

        return ReviewsCount()
    else:
        return reviews_count


def add_reviews_count(model: str, place: ReviewsCount, db: Session = test()):
    db_model = {
        'flamp': FlampReviewCount,
        'doublegis': DoubleGisReviewCount
    }

    new_place = db_model[model](
        place_id=place.place_id,
        reviews_count=place.reviews_count
    )
    db.add(new_place)
    db.commit()
    db.refresh(new_place)

    return new_place


def update_reviews_count(model: str, update_place: ReviewsCount, db: Session = test()):
    db_model = {
        'flamp': FlampReviewCount,
        'doublegis': DoubleGisReviewCount
    }
    reviews_count = db.query(db_model[model]).filter(db_model[model].place_id == update_place.place_id).first()
    if reviews_count is None:

        new_place = db_model[model](
            place_id=update_place.place_id,
            reviews_count=update_place.reviews_count
        )
        db.add(new_place)
        db.commit()
        db.refresh(new_place)

        return new_place

    else:
        db.query(db_model[model]).filter(db_model[model].place_id == update_place.place_id).update(
            {'reviews_count': update_place.reviews_count})

        db.commit()


def delete_review(db: Session = test()):
    # flamp_review_count
    # review
    query = 'DELETE FROM flamp_review_count'
    db.execute(query)
    db.commit()

# if __name__ == '__main__':
#     delete_review()
