from celery import Celery
from app.core.properties import REDIS_BROKER, REDIS_BACKEND

app = Celery(
    'background_parser',
    broker=REDIS_BROKER,
    backend=REDIS_BACKEND,
    include=['background_parser.tasks']
)


if __name__ == '__main__':
    app.start()