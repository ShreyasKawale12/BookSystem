from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=20, blank=True)
    books = models.ManyToManyField('book.Book', through='Inventory', related_name='books')
    customers = models.ManyToManyField('auth.User', through='Quantity', related_name='stores')

    def __str__(self):
        return self.name


class Inventory(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="store_inventory")
    book = models.ForeignKey('book.Book', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['store', 'book'], name='unique_book_per_store')
        ]


class Quantity(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store_quantity')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='user_quantity')
    book = models.ForeignKey('book.Book', on_delete=models.CASCADE, related_name='book_quantity')
    quantity = models.PositiveIntegerField(default=0)
    
