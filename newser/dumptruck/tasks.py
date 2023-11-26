from celery import shared_task
from .management import dump_database

@shared_task
def dump_database_data():
    dump_database('data')
