from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "newser.news"
    verbose_name = _("News")

    def ready(self):
        try:
            import newser.news.signals  # noqa: F401
        except ImportError:
            pass
