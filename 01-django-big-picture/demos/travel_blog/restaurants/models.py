from django.conf import settings
from django.db import models
from django.utils import timezone

from trips.models import Trip, Picture


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    name = models.CharField("Name of the venue", max_length=300)
    intro_text = models.TextField()
    main_picture = models.ForeignKey(Picture, on_delete=models.CASCADE, blank=True)

    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
