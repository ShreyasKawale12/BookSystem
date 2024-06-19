from django.contrib import admin

from .models import Book, Author, Publisher
import django_filters
from django_admin_multi_select_filter.filters import MultiSelectFieldListFilter


class BookFilter(admin.SimpleListFilter):
    title = 'Price Filter'
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return [
            ('less_than_200', 'Less than 200'),
            ('200_to_500', '200 to 500'),
            ('greater_than_500', 'greater than 500')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'less_than_200':
            return queryset.filter(price__lte=200)
        if self.value() == '200_to_500':
            return queryset.filter(price__gt=200, price__lt=500)
        if self.value() == 'greater_than_500':
            return queryset.filter(price__gte=500)
        return queryset


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'publisher', 'price']
    list_display = ['title', 'author', 'publisher']
    list_filter = [('author__name', MultiSelectFieldListFilter), 'publisher', BookFilter]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ['name', 'user']
    list_display = ['name', ]


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    fields = ['name', ]
    list_display = ['name', ]

# Register your models here.
