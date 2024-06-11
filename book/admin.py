from django.contrib import admin

from .models import Book, Author, Publisher


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'publisher', 'price']
    list_display = ['title', 'author', 'publisher']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ['name', 'user']
    list_display = ['name', 'user']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    fields = ['name', ]
    list_display = ['name', ]

# Register your models here.
