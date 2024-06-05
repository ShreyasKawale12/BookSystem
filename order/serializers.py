from rest_framework import serializers
from .models import Order, OrderItem
from book.models import Book
from store.models import Store


class OrderItemSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    store = serializers.PrimaryKeyRelatedField(queryset=Store.objects.all())

    class Meta:
        model = OrderItem
        fields = ['book', 'store', 'quantity', 'price']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    user = serializers.ReadOnlyField(source='user.username')
    confirm_order = serializers.BooleanField(write_only= True)

    def create(self, validated_data):
        validated_data.pop("confirm_order")
        order = Order.objects.create(**validated_data)
        return order

    class Meta:
        model = Order
        fields = ['user', 'created_at', 'status', 'total_amount', 'order_items', 'confirm_order']
        read_only_fields = ['created_at', 'status', 'total_amount', 'order_items']
