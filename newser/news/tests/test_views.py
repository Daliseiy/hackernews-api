import pytest
from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model
from newser.news.models import Story

from newser.news.views import story_list, story_detail

User = get_user_model()


@pytest.fixture
def factory():
    return RequestFactory()


@pytest.fixture
def create_test_story(db):
    def _create_test_story(**kwargs):
        return Story(**kwargs)
    return _create_test_story

def test_create_story(db, create_test_story):
    # Create a test story
    test_story = create_test_story(
        id = 1293,
        title="Sample Story",
        content="This is a sample story",
        deleted=False,
        by="Author",
        time="2023-09-07T12:00:00Z",
        score=10,
        url="http://example.com",
        type="story",
        source="user"
    )

    # Assertions
    assert test_story.id is not None  # Check that the ID is not null
    assert test_story.title == "Sample Story" 


def test_story_list_view(db, create_test_story, factory):
    # Create test stories
    for i in range(10):
        create_test_story(
            title=f"Test Story {i}",
            content=f"This is test story {i}",
            type="story"
        )

    # Create a GET request to the story_list view
    url = reverse('mews')
    request = factory.get(url)

    # Use the view function to process the request
    response = story_list(request)

    # Assertions
    assert response.status_code == 200
    assert len(response.context['stories']) == 10  # Assuming 10 stories were created

# Test for the story_detail view
def test_story_detail_view(db, create_test_story, factory):
    # Create a test story
    test_story = create_test_story(
        title="Test Story",
        content="This is a test story",
        type="story"
    )

    # Create a GET request to the story_detail view
    url = reverse('news:story_detail', args=[test_story.id])
    request = factory.get(url)

    # Use the view function to process the request
    response = story_detail(request, story_id=test_story.id)

    # Assertions
    assert response.status_code == 200
    assert response.context['story'] == test_story