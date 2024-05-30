from django.db import models

# Create your models here.
from book.models import Book


class Store(models.Model):
    name = models.CharField(max_length=20, blank=True)
    books = models.ManyToManyField(Book, through='Inventory', related_name='books')

    def __str__(self):
        return self.name


class Inventory(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="store_inventory")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
