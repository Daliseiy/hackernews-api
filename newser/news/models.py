from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Story(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, default="No Title")
    content = models.TextField(blank=True)
    deleted = models.BooleanField(default=False)
    by = models.CharField(max_length=150, blank=True)
    time = models.DateTimeField(blank=True)
    score = models.IntegerField(null=True, blank=True)
    url = models.URLField(blank=True)
    type = models.CharField(
        max_length=10,
        choices=[("job", "job"), ("story", "story"), ("comment", "comment"), ("poll", "poll"), ("pollopt", "pollopt")],
    )
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)  # Associate a User with the Story

    source = models.CharField(
        max_length=20,
        choices=[
            ("hackernews", "Hacker News"),
            ("user", "User"),
        ],
        default="user   ",
    )

    def __str__(self):
        return f"Story: {self.title}"
