from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Cart, BookQuantity
from store.models import Inventory
@receiver(post_save, sender =BookQuantity)
def cart_post_save(sender, instance, created, **kwargs):
    pass