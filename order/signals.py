from django.db import transaction
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.http import Http404

from .models import Order
from store.models import Inventory


@receiver(pre_save, sender=Order)
def order_post_save(sender, instance, **kwargs):
    with transaction.atomic():
        user = instance.user
        user_cart = user.user_cart
        book_quantities = user_cart.book_quantity.all()

        for bq in book_quantities:
            store = bq.store
            book = bq.book
            quantity = bq.quantity
            try:
                inventory = Inventory.objects.select_for_update().get(store=store, book=book)
                if quantity < inventory.quantity:
                    # raise ValidationError(f"{book} is out of stock -> Available stock = {inventory.quantity}")
                    inventory.quantity -= quantity
                    inventory.save()
                else:
                    instance.status = 'FAILED'
                    instance.order_message = f"Book {book} is out of stock -> Available stock = {inventory.quantity}"
            except Inventory.DoesNotExist:
                instance.status = 'FAILED'
                instance.order_message = f"Inventory for {book} does not exist"
