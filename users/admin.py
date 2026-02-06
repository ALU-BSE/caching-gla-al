from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'user_type', 'is_staff')
    list_filter = ('user_type', 'is_staff')
    search_fields = ('email', 'phone_number')
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)