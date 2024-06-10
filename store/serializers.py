from rest_framework import serializers
from .models import Inventory, Store, Quantity
from order.serializers import OrderItemSerializer, OrderSerializer


class InventorySerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.title', read_only=True)

    class Meta:
        model = Inventory
        fields = ['book', 'book_title', 'quantity']


class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quantity
        fields = ['store', 'user', 'book', 'quantity']


class StoreSerializer(serializers.ModelSerializer):
    inventory = InventorySerializer(source='store_inventory', many=True, read_only=True)
    orders = serializers.SerializerMethodField()

    class Meta:
        model = Store
        fields = ['id', 'name', 'inventory','orders']

    def get_orders(self, instance):
        order_items = instance.order_items.all()
        orders = {item.order for item in order_items}
        return OrderSerializer(orders, many=True).data
