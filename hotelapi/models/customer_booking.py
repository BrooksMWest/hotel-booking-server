from django.db import models
from .booking import Booking
from .customer import Customer

class CustomerBooking(models.Model):
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE, related_name='customer_bookings')
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='bookings')
