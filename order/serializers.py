from rest_framework import serializers
from .models import Order, OrderItem
from book.models import Book
from store.models import Store
from cart.serializers import BookQuantitySerializer


class OrderItemSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    store = serializers.PrimaryKeyRelatedField(queryset=Store.objects.all())

    class Meta:
        model = OrderItem
        fields = ['id','book', 'store', 'quantity', 'price',]


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    user = serializers.ReadOnlyField(source='user.username')
    confirm_order = serializers.BooleanField(write_only=True)

    def create(self, validated_data):
        validated_data.pop("confirm_order")
        order = Order.objects.create(**validated_data)
        return order

    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'status', 'total_amount', 'order_items', 'confirm_order']
        read_only_fields = ['created_at', 'status', 'total_amount', 'order_items']


class OrderSerializerForStore(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'status', 'order_items']


class CancelOrderSerializer(serializers.Serializer):
    order_id = serializers.PrimaryKeyRelatedField(queryset=Order.objects.filter(status='Active'), required=True)

    def validate_order_id(self, value):
        return value
