from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'first_name', 'email', 'phone_number', 'is_superuser', 'status')

admin.site.register(CustomUser, CustomUserAdmin)