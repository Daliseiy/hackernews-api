import datetime
import time
import requests
from .models import Story  


def get_top_news_ids():
    url = "https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty"
    response = requests.get(url)

    if response.status_code == 200:
        top_news_ids = response.json()
        return top_news_ids
    else:
        print("Failed to retrieve top news IDs.")
        return []


def get_news_details(news_id):
    url = f"https://hacker-news.firebaseio.com/v0/item/{news_id}.json?print=pretty"
    response = requests.get(url)

    if response.status_code == 200:
        news_data = response.json()
        return news_data
    else:
        return None


def create_story(news_data):
    story = Story(
        id=news_data.get("id"),
        title=news_data.get("title", "No Title"),
        deleted=news_data.get("deleted", False),
        by=news_data.get("by", ""),
        time=datetime.datetime.fromtimestamp(news_data.get("time", 0)),
        score=news_data.get("score", None),
        url=news_data.get("url", ""),
        type=news_data.get("type", "story"),
        user=None,  # Set the user field based on the source
        source="hackernews",  
    )
    story.save()
    print("Story operation Succesful")
    return story


def create_news_data():
    top_news_ids = get_top_news_ids()

    if top_news_ids:
        for news_id in top_news_ids:  # Fetching details for the all the news items
            time.sleep(2.5)
            news_data = get_news_details(news_id)
            if news_data:
                print(f'Title: {news_data["title"]}')
                create_story(news_data)
