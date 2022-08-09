from datetime import datetime

from app.crud import add_new_review, get_user_data, get_all_users
from app.flamp_parser import FlampParser
from app.schemas import ReviewBase, UserBase


def wrapper(func):
    def inner(*args, **kwargs):
        now = datetime.now()
        result = func(*args, **kwargs)
        print('Времени прошло', datetime.now() - now)
        return result

    return inner


@wrapper
def get_reviews(api):
    user_list = get_all_users()

    for review in api():
        save_review(ReviewBase(**review))
        for user in user_list:
            send_review(user.id, review)


def save_review(review: ReviewBase):
    add_new_review(review)


def create_new_user(user: UserBase):
    get_user_data(user)


def get_current_user(func):
    def inner(*args, **kwargs):
        user = get_user_data(args[0])
        if user.is_active:
            return func(*args, **kwargs)

    return inner


@get_current_user
def send_review(chat_id: int, review):
    print(f'{chat_id}\n{review}')


if __name__ == '__main__':
    get_reviews(FlampParser().check_new_reviews)
