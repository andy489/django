from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Destination(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100, default="")
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.country}"


class Picture(models.Model):
    image = models.ImageField(blank=True)
    name = models.CharField(max_length=100)
    caption = models.CharField(max_length=300, blank=True)

    @property
    def url(self):
        return self.image.url

    def __str__(self):
        return self.name


class Trip(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    destination = models.ForeignKey(Destination, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    intro_text = models.TextField()
    main_picture = models.ForeignKey(Picture, on_delete=models.PROTECT, blank=True)

    created_date = models.DateTimeField(default=timezone.now)
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        get_latest_by = ["to_date", "from_date"]
        ordering = ["-from_date"]

    def get_absolute_url(self):
        return reverse("trip_detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.title


class Paragraph(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    order = models.IntegerField(default=1)
    article = models.ForeignKey(
        Trip, on_delete=models.PROTECT, related_name="paragraphs"
    )
    picture = models.ForeignKey(Picture, blank=True, on_delete=models.PROTECT)

    class Meta:
        unique_together = ["article", "order"]
        ordering = ["article_id", "order"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField("Your name", max_length=100)
    text = models.TextField("Your comment")
    created_date = models.DateTimeField(default=timezone.now)
