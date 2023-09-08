from django.urls import include, path

from . import views

app_name = 'news'
urlpatterns = [
    path('', views.story_list, name='story_list'),
    path('<int:story_id>/', views.story_detail, name='story_detail'),
]
