from django.contrib import admin
from .models import Store, Inventory


class InventoryInline(admin.TabularInline):
    model = Inventory
    extra = 1


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']
    inlines = [InventoryInline]


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    fields = ['store', 'book', 'quantity']
    list_display = ['store', 'book', 'quantity']
