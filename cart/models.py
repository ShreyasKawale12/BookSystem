from django.db import models


class Cart(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='user_cart')
    store = models.OneToOneField('store.Store', on_delete=models.CASCADE, related_name='store_cart')
    books = models.ManyToManyField('book.Book', through='BookQuantity', related_name='+')


class BookQuantity(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='book_quantity')
    book = models.ForeignKey('book.Book', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
