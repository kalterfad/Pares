from celery.schedules import crontab

from app.celery_conf.celery import app

@app
def update_reviews():
    pass



app.conf.beat_schedule = {
    'update_reviews': {
        'task': 'sociable_enwor.tasks.send_update',
        'schedule': crontab(minute='*/20', hour='7-18', day_of_week='mon,tue,wed,thu,fri,sat'),
    }
}