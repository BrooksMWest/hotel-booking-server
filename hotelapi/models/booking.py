from django.db import models
from .event import Event


class Booking(models.Model):
    paid = models.BooleanField(default=False)
    number_of_party = models.IntegerField()
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
