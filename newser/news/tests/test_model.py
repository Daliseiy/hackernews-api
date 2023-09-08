from django.test import TestCase
from django.contrib.auth import get_user_model

from newser.news.models import Story

User = get_user_model()

def setUpTestData():
        # Create a user for testing
        return User(
            username='testuser',
            email="testemail@email.com",
            password='testpassword'
)

def test_create_story(title="Sample Story", content="This is a sample story", deleted=False, by="Author", time="2023-09-07T12:00:00Z", score=10, url="http://example.com", type="story", source="user"):
    
    user = setUpTestData()
    story =  Story(
            title=title,
            content=content,
            deleted=deleted,
            by=by,
            time=time,
            score=score,
            url=url,
            type=type,
            user=user,
            source=source
        )


    assert isinstance(story, Story)
    assert story.title == title
    assert story.content == content
    assert story.deleted == deleted
    assert story.by == by
    assert story.time == time
    assert story.score == score
    assert story.url == url
    assert story.type == type
    assert story.source == source
    assert story.user == user



