from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Cart, BookQuantity
from book.models import Book
from store.models import Store


class BookQuantitySerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    store = serializers.PrimaryKeyRelatedField(queryset=Store.objects.all())

    class Meta:
        model = BookQuantity
        fields = ['book', 'store', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    book_quantity = BookQuantitySerializer(many=True)
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Cart
        fields = ['user', 'book_quantity', ]

    def create(self, validated_data):
        book_quantities_data = validated_data.pop('book_quantity')
        cart = Cart.objects.create(user=self.context['request'].user)
        for book_quantity_data in book_quantities_data:
            BookQuantity.objects.create(cart=cart, **book_quantity_data)
        return cart

    def update(self, instance, validated_data):
        # Handle the book quantities separately
        book_quantities_data = validated_data.pop('book_quantity', [])

        # Update the cart instance with any other fields
        super().update(instance, validated_data)

        # Update or create book quantity instances
        for book_quantity_data in book_quantities_data:
            book_instance = book_quantity_data.get('book')
            store_instance = book_quantity_data.get('store')
            quantity = book_quantity_data.get('quantity')

            book_quantity_instance, created = BookQuantity.objects.update_or_create(
                cart=instance,
                book=book_instance,
                store=store_instance,
                defaults={
                    'book': book_instance,
                    'store': store_instance,
                    'quantity': quantity}
            )

        return instance


class CartSerializerForOrders(serializers.ModelSerializer):
    book_list = BookQuantitySerializer(source='book_quantity', many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['book_list']
