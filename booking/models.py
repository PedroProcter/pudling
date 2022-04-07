from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.TextField(max_length=50)
    lastname = models.TextField(max_length=50)
    email = models.TextField(max_length=50)

class Booking(models.Model):
    client = models.ForeignKey(Client, related_name='booked_by', on_delete=models.CASCADE)
    begins_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=50.00)
    comment = models.TextField(max_length=250)
    canceled = models.BooleanField(default=False)
    payed = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)

class Room(models.Model):
    name = models.TextField(max_length=50, default='Pudling Pet\'s Room')
    reserved = models.BooleanField()
    is_active = models.BooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class RoomType(models.Model):
    room = models.ForeignKey(Room, on_delete=models.PROTECT, default=0)
    size = models.TextField(max_length=4)
    accepted_species = models.TextField(max_length=20)
    description = models.TextField(max_length=100)

class RoomBooking(models.Model):
    room_brand = models.ForeignKey(Room, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

class FoodBrand(models.Model):
    name = models.TextField(max_length=50)
    is_active = models.BooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class FoodType(models.Model):
    food_brand = models.ForeignKey(FoodBrand, on_delete=models.PROTECT, default=0)
    accepted_species = models.TextField(max_length=20)
    description = models.TextField(max_length=100)

class FoodBrandBooking(models.Model):
    food_brand = models.ForeignKey(FoodBrand, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)