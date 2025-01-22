from django.db import models

class CustomerBooking(models.Model):
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE, related_name='customer_bookings')
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='bookings')
