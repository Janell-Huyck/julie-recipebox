from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    favorites = models.ManyToManyField(
        "NewsItem", symmetrical=False, blank=True, related_name="favorites"
    )

    def __str__(self):
        return self.name


class NewsItem(models.Model):
    title = models.CharField(max_length=30)
    time_required = models.CharField(max_length=30)
    description = models.TextField()
    instructions = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
