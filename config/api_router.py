from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from newser.news.api.views import StoryViewSet
from newser.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register(r"stories", StoryViewSet)


app_name = "api"
urlpatterns = router.urls
