from django.db import models

class Events(models.Model):
    event_name = models.CharField(max_length=255)
    date = models.DateTimeField()
    time = models.TimeField()

  