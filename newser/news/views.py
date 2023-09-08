from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from .models import Story


def story_list(request):
    stories = Story.objects.order_by('-time')

    story_type = request.GET.get('type')
    if story_type:
        stories = stories.filter(type=story_type)

    search_text = request.GET.get('search')
    if search_text:
        stories = stories.filter(title__icontains=search_text)

    # Paginate the stories with a limit of 50 per page
    paginator = Paginator(stories, 50)

    try:
        page_number = request.GET.get('page')
        stories = paginator.page(page_number)
    except PageNotAnInteger:
        stories = paginator.page(1)
    except EmptyPage:
        stories = paginator.page(paginator.num_pages)

    return render(request, 'news/story_list.html', {
        'stories': stories,
        'search_text': search_text,  # Pass the search text back to the template
        'story_type': story_type,    # Pass the story type back to the template
    })


def story_detail(request, story_id):
    # Get the specific story by its ID or return a 404 error if not found
    story = get_object_or_404(Story, id=story_id)

    return render(request, 'news/story_detail.html', {'story': story})
