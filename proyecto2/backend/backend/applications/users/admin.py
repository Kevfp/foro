from django.contrib import admin
from .models import User


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    fields = ["username", "email", "name", "surname", "is_staff"]
    list_display = ["username", "email", "name", "surname", "is_staff"]

admin.site.register(User, UserAdmin)