from rest_framework import serializers
from .models import Inventory, Store


class InventorySerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.title', read_only=True)

    class Meta:
        model = Inventory
        fields = ['book', 'book_title', 'quantity']



class StoreSerializer(serializers.ModelSerializer):
    inventory = InventorySerializer(source='store_inventory', many=True, read_only=True)

    class Meta:
        model = Store
        fields = ['id', 'name', 'inventory']
