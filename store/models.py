from django.db import models

# Create your models here.
from book.models import Book


class Store(models.Model):
    name = models.CharField(max_length=20, blank=True)
    books = models.ManyToManyField(Book, related_name='books')
