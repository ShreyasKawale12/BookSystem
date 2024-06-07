from django.db import models


class Cart(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='user_cart')
    books = models.ManyToManyField('book.Book', through='BookQuantity', related_name='+')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user'], name='unique_cart_per_user')
        ]


class BookQuantity(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='book_quantity')
    store = models.ForeignKey('store.Store', on_delete=models.CASCADE, related_name='+', default=1)
    book = models.ForeignKey('book.Book', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)


