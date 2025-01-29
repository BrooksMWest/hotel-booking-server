from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=255)
    description = models.TextField(max_length=500, null=True, blank=True, default="")
    image_url = models.URLField(max_length=500, null=True, blank=True, default="")
    date = models.DateField()
    time = models.TimeField()

  