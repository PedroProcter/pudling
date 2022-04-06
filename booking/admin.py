from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'lastname', 'email']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = [
        'client', 
        'begins_at', 
        'ends_at',
        'cost', 
        'comment',
        'canceled', 
        'payed', 
        'closed'
        ]
    list_filter = [
        'client', 
        'begins_at', 
        'ends_at',
        'cost', 
        'canceled', 
        'payed', 
        'closed'
    ]
    list_editable = [ 
        'begins_at', 
        'ends_at',
        'cost', 
        'canceled', 
        'payed', 
        'closed'
    ]

@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = [
        'size',
        'species',
        'description',
    ]
    
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'reserved',
        'is_active',
        'price',
        'category_id'
    ]

@admin.register(RoomBooking)
class RoomBookingAdmin(admin.ModelAdmin):
    list_display = [
        'booking_id',
        'room_brand_id',
    ]

@admin.register(FoodType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = [
        'species',
        'description',
    ]
    
@admin.register(FoodBrand)
class FoodBrandAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'is_active',
        'price',
        'category_id'
    ]

@admin.register(FoodBrandBooking)
class FoodBrandBookingAdmin(admin.ModelAdmin):
    list_display = [
        'booking_id',
        'food_brand_id',
    ]