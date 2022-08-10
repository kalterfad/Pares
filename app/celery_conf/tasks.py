import telebot
from celery.schedules import crontab

from app.bot_process import get_reviews
from app.celery_conf.celery import app
from app.core.properties import bot
from app.parser.flamp_parser import FlampParser
from app.parser.double_gis_parser import DoubleGisParser


@app
def update_reviews():
    a = FlampParser().check_new_reviews
    b = DoubleGisParser().check_new_reviews
    get_reviews()


def try_send_message(chat_id, message, keyboard=None):
    try:
        bot.send_message(chat_id, message, parse_mode='html')
    except telebot.apihelper.ApiException:
        pass
        # process.delete_user(chat_id)


app.conf.beat_schedule = {
    'update_reviews': {
        'task': 'app.celery_conf.tasks.update_reviews',
        'schedule': crontab(minute=0, hour=0, day_of_week='mon,tue,wed,thu,fri,sat'),
    }
}