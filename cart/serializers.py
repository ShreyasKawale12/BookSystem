from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Cart, BookQuantity


class BookQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookQuantity
        fields = ['store', 'book', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    book_quantity = BookQuantitySerializer(many=True, read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Cart
        fields = ['user', 'username','book_quantity',]
