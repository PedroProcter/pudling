from django.shortcuts import render
from .models import *

# Create your views here.
def get_all_rooms():
    return Room.objects.all()

def get_all_food_brands():
    return FoodBrand.objects.all()

def booking(request):
    rooms = get_all_rooms()
    food_brands = get_all_food_brands()
    return render(request, 'booking.html', {'rooms':rooms, 'food_brands':food_brands})

def reservations(request):
    rooms = get_all_rooms()
    food_brands = get_all_food_brands()
    return render(request, 'reservation.html', {'rooms':rooms, 'food_brands':food_brands})

def rooms(request):
    return render(request, 'rooms.html')

def food_brands(request):
    return render(request, 'food_brands.html')