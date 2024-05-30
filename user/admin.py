from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

admin.site.unregister(User)


# Register your models here.

class UserAdmin(DefaultUserAdmin):
    list_display = ['first_name', 'last_name']


admin.site.register(User, UserAdmin)
