from django.db import models
from hotelapi.models.booking import Booking

class Room(models.Model):

  room_number = models.IntegerField()
  vacancy = models.BooleanField()
  room_size = models.IntegerField(max_length=5)
  star_rating = models.IntegerField(max_length=5)
  price = models.CharField(max_length=10)
  good_view = models.BooleanField()
  smoking = models.BooleanField()
  booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
