from celery.schedules import crontab

from bot_process.bot_process import get_reviews
from celery_conf.celery import app
from parser.double_gis_parser import DoubleGisParser
from parser.flamp_parser import FlampParser


@app.task
def update_reviews_from_flamp():
    get_reviews(FlampParser().check_new_reviews)


@app.task
def update_reviews_from_double_gis():
    get_reviews(DoubleGisParser().check_new_reviews)


app.conf.beat_schedule = {
    'update_reviews_from_flamp': {
        'task': 'celery_conf.tasks.update_reviews_from_flamp',
        'schedule': crontab(minute='*/8', hour='2-21')
    },
    'update_reviews_from_double_gis': {
        'task': 'celery_conf.tasks.update_reviews_from_double_gis',
        'schedule': crontab(minute=10, hour=20)
    }
}
