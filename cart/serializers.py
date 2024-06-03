from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Cart, BookQuantity


class BookQuantitySerializer(serializers.ModelSerializer):
    book_title = serializers.SerializerMethodField()
    store_name = serializers.SerializerMethodField()

    def get_book_title(self, obj):
        return obj.book.title

    def get_store_name(self, obj):
        return obj.store.name

    class Meta:
        model = BookQuantity
        fields = ['store_name', 'book_title', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    book_quantity = BookQuantitySerializer(many=True, read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Cart
        fields = ['user', 'username', 'book_quantity', ]


class CartSerializerForOrders(serializers.ModelSerializer):
    book_list = BookQuantitySerializer(source='book_quantity', many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['book_list']
