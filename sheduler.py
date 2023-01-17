from celery import Celery
from setting import Config


def make_celery() -> Celery:
    celery = Celery(
        'app',
        broker=Config.REDIS_URL,
        backend=Config.REDIS_URL,
        include=[
            "components.videos.tasks"
        ]
    )

    return celery


celery = make_celery()