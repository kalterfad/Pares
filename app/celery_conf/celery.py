from celery import Celery
from app.core.properties import REDIS_BROKER, REDIS_BACKEND

app = Celery(
    'celery_conf',
    broker=REDIS_BROKER,
    backend=REDIS_BACKEND,
    include=['celery_conf.tasks']
)

app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    result_expires=3600,
    timezone='Asia/Yekaterinburg',
    enable_utc=True,
)
app.autodiscover_tasks()

if __name__ == '__main__':
    app.start()