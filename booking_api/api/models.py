from django.db import models

class Availability(models.Model):
    user = models.CharField(max_length=100)
    weekday = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

class Booking(models.Model):
    guest_name = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
