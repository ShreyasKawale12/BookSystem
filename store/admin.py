from django.contrib import admin
from .models import Store, Inventory, Quantity


class InventoryInline(admin.TabularInline):
    model = Inventory
    extra = 1


class QuantityInline(admin.TabularInline):
    model = Quantity
    extra = 1


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']
    inlines = [InventoryInline, QuantityInline]


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    fields = ['store', 'book', 'quantity']
    list_display = ['store', 'book', 'quantity']


@admin.register(Quantity)
class QuantityAdmin(admin.ModelAdmin):
    fields = ['store', 'user', 'book', 'quantity']
