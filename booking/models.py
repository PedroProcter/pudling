import re
from django.db import models
from datetime import datetime

# Create your models here.
class Client(models.Model):
    name = models.TextField(max_length=50)
    lastname = models.TextField(max_length=50)
    email = models.TextField(max_length=50)

class Booking(models.Model):
    client = models.ForeignKey(Client, related_name='booked_by', on_delete=models.CASCADE)
    begins_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=4, default=50.00)
    comment = models.TextField(max_length=250)
    canceled = models.BooleanField(default=False)
    payed = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)

class RoomType(models.Model):
    size = models.TextField(max_length=4)
    species = models.TextField(max_length=20)
    description = models.TextField(max_length=100)

class Room(models.Model):
    name = models.TextField(max_length=50, default='Pudling Pet\'s Room')
    category = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    reserved = models.BooleanField()
    is_active = models.BooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=4)

class RoomBooking(models.Model):
    room_brand = models.ForeignKey(Room, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

class FoodType(models.Model):
    size = models.TextField(max_length=4)
    species = models.TextField(max_length=20)
    description = models.TextField(max_length=100)

class FoodBrand(models.Model):
    name = models.TextField(max_length=50)
    category = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    is_active = models.BooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=4)

class FoodBrandBooking(models.Model):
    food_brand = models.ForeignKey(FoodBrand, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)