from django.db import transaction
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.http import Http404

from .email_utils import send_order_out_for_delivery_email
from .models import Order, OrderItem
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


@receiver(post_save, sender=OrderItem)
def order_item_post_save(sender, instance, created, **kwargs):
    if not created and instance.out_for_delivery:
        status = True
        order = instance.order
        order_items = order.order_items.all()
        for item in order_items:
            status = status and item.out_for_delivery
            print(status)
        if status:
            order.status = 'confirmed'
            order.save()
            send_order_out_for_delivery_email(order)
