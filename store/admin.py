from django.contrib import admin
from .models import Store, Inventory


class InventoryInline(admin.TabularInline):
    model = Inventory
    extra = 1


# class QuantityInline(admin.TabularInline):
#     model = Quantity
#     extra = 1


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    fields = ['name','owner' ]
    list_display = ['name', 'owner']
    inlines = [InventoryInline,]


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    fields = ['store', 'book',]
    list_display = ['store', 'book',]


# @admin.register(Quantity)
# class QuantityAdmin(admin.ModelAdmin):
#     fields = ['store', 'user', 'book', 'quantity']


