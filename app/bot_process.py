from app.crud import add_new_review, get_user_data, get_all_users
from app.double_gis_parser import DoubleGisParser
from app.flamp_parser import FlampParser
from app.schemas import ReviewBase


def get_reviews(api):
    user_list = get_all_users()

    for review in api():
        for user in user_list:
            send_review(user.id, review)
            # save_review(ReviewBase(**review))


def save_review(review: ReviewBase):
    add_new_review(review)


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
    get_reviews(DoubleGisParser().collect_result)
