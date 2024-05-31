from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Quantity, Inventory


@receiver(post_save, sender=Quantity)
def update_inventory(sender, instance, created, **kwargs):
    inventory = Inventory.objects.get(store=instance.store, book=instance.book)
    inventory.quantity -= instance.quantity
    inventory.save()
    if inventory.quantity == 0:
        inventory.delete()
