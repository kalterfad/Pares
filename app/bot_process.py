from app.flamp_parser import FlampParser
from app.crud import add_new_review, get_user_data
from app.schemas import ReviewBase, UserBase


def get_reviews():
    flamp = FlampParser().get_reviews()


def save_review(review: ReviewBase):
    add_new_review(review)


def get_current_user(func):
    def inner(*args, **kwargs):
        user = get_user_data(kwargs['chat_id'])
        if user.is_active:
            return func(*args, **kwargs)

    return inner


@get_current_user
def send_review(chat_id, name, test):
    print(chat_id)







if __name__ == '__main__':
    send_review(chat_id=12314124, name='ftira', test=12)