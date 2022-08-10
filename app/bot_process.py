import re
from datetime import datetime

from app.core.properties import bot
from app.database.crud import add_new_review, get_user_data, get_all_users
from app.parser.flamp_parser import FlampParser
from app.parser.double_gis_parser import DoubleGisParser
from app.database.schemas import ReviewBase, UserBase


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
        print(ReviewBase(**review).website)
        # for user in user_list:
        #     send_review(user.id, ReviewBase(**review))


def save_review(review: ReviewBase):
    add_new_review(review)


def create_new_user(user: UserBase):
    get_user_data(user)


def get_current_user(func):
    def inner(*args, **kwargs):
        user = get_user_data(UserBase(**{'id': args[0]}))
        if user.is_active:
            return func(*args, **kwargs)

    return inner


@get_current_user
def send_review(chat_id: int, review: ReviewBase):

    date_created = re.search('\\d{4}-\\d{2}-\\d{2}?', review.date_created).group()
    review_link = f'<a href = "{review.website}">Ссылка на отзыв</a>'

    message = f'<b>Появился новый отзыв!</b>\n\n' \
              f'{review_link}\n' \
              f'<b>Дата:</b> {date_created}\n' \
              f'<b>Пользователь:</b> {review.user}\n' \
              f'<b>Рейтинг:</b>: {review.rating}\n\n' \
              f'<b>Отзыв</b>: {review.text}'
    try:
        bot.send_message(chat_id, message, parse_mode='html', disable_web_page_preview=True)
    except Exception as e:
        print(e)
    print(review)


if __name__ == '__main__':
    get_reviews(DoubleGisParser().check_new_reviews)
