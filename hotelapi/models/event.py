from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    image_url = models.CharField(max_length=255)
    date = models.DateTimeField()
    time = models.TimeField()

  