from django.contrib import admin
from .models import Cart, BookQuantity


class BookQuantityInline(admin.TabularInline):
    model = BookQuantity
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)
    fields = ('user', 'store')
    inlines = [
        BookQuantityInline,
    ]
