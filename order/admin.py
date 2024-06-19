from django.contrib import admin
from .models import Order


# Register your models here.
class OrderCustomFilter(admin.SimpleListFilter):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ['user']
