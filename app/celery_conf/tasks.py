from celery.schedules import crontab

from app.bot_process import get_reviews
from app.celery_conf.celery import app
from app.parser.flamp_parser import FlampParser
from app.parser.double_gis_parser import DoubleGisParser


@app
def update_reviews_from_flamp():
    get_reviews(FlampParser().check_new_reviews)


@app
def update_reviews_from_double_gis():
    get_reviews(DoubleGisParser().check_new_reviews)


app.conf.beat_schedule = {
    'update_reviews_from_flamp': {
        'task': 'app.celery_conf.tasks.update_reviews_from_flamp',
        'schedule': crontab(minute=0, hour=0),
    },
    'update_reviews_from_double_gis': {
            'task': 'app.celery_conf.tasks.update_reviews_from_double_gis',
            'schedule': crontab(minute=0, hour=0),
    }
}
