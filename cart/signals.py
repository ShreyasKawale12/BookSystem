from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

from .models import Cart, BookQuantity
from store.models import Inventory


@receiver(pre_save, sender=BookQuantity)
def cart_pre_save(sender, instance, **kwargs):
    store = instance.store
    book = instance.book
    requested_quantity = instance.quantity
    try:
        inventory = Inventory.objects.get(store=store, book=book)
        if inventory.quantity < requested_quantity:
            raise ValidationError(f"Insufficient copies of {book.title}, Available copies = {inventory.quantity}")
    except Inventory.DoesNotExist:
        raise ValidationError(f"{book.title} is not available in store {store.name}")


@receiver(post_save, sender= BookQuantity)
def book_quantity_post_save(sender, instance, created, **kwargs):
    pass





