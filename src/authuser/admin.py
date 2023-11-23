from django.contrib import admin
from authuser.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined']
