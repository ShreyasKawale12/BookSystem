from django.contrib import admin

from .models import Book, Author, Publisher, Distribution


class DistributionInline(admin.TabularInline):
    model = Distribution
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'publisher', ]
    list_display = ['title', 'author', 'publisher']
    inlines = [
        DistributionInline,
    ]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ['name', ]
    list_display = ['name', ]


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    fields = ['name', ]
    list_display = ['name', ]


# Register your models here.

@admin.register(Distribution)
class DistributionAdmin(admin.ModelAdmin):
    fields = ['book', 'store', 'user', 'quantity']
