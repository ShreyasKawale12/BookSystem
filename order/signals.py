from django.db import transaction
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.http import Http404

from .models import Order
from store.models import Inventory


@receiver(post_save, sender=Order)
def order_post_save(sender, instance, created, **kwargs):
    if created:
        print("order_post_save signal called for new order")
        with transaction.atomic():
            user = instance.user
            user_cart = user.user_cart
            book_quantities = user_cart.book_quantity.all()

            for book_quantity in book_quantities:
                store = book_quantity.store
                book = book_quantity.book
                quantity = book_quantity.quantity

                inventory = Inventory.objects.select_for_update().get(store=store, book=book)
                inventory.quantity -= quantity
                inventory.save()
    else:
        print("order_post_save signal called for order update")



