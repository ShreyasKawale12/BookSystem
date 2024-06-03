from rest_framework import serializers
from cart.serializers import CartSerializerForOrders
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    products = CartSerializerForOrders(read_only=True, source='user.user_cart')

    class Meta:
        model = Order
        fields = ['user', 'created_at', 'status', 'total_amount', 'products', 'order_message']
        read_only_fields = ['created_at', 'status', 'total_amount', 'products', 'order_message']
