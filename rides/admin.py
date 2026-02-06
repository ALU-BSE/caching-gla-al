from django.contrib import admin
from .models import Ride

@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ('id', 'passenger', 'rider', 'status', 'fare', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('passenger__email', 'rider__email', 'pickup_address')
    ordering = ('-created_at',)