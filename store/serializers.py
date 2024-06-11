from rest_framework import serializers

from order.models import OrderItem
from .models import Inventory, Store, Quantity
from order.serializers import OrderItemSerializer, OrderSerializerForStore


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
    order_items = serializers.SerializerMethodField()
    order_item_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Store
        fields = ['id', 'name', 'inventory', 'order_items', 'order_item_id']
        read_only_fields = ['name', ]

    def update(self, instance, validated_data):
        order_item_id = validated_data.pop('order_item_id')
        print(order_item_id)
        super().update(instance, validated_data)
        order_item = OrderItem.objects.get(id=order_item_id)
        order_item.out_for_delivery = True
        order_item.save()

        return instance

    def get_order_items(self, instance):
        queryset = OrderItem.objects.select_related('order').filter(store=instance, out_for_delivery=False).exclude(order__status='Cancelled')
        return OrderItemSerializer(queryset, many=True).data
