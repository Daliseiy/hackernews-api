from django.contrib.auth import get_user_model

from config import celery_app

from .jobs import create_news_data

User = get_user_model()


# @celery_app.task(time_limit=250)
# def get_news_data():
#     create_news_data()
