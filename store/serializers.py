from rest_framework import serializers
from .models import Store
from book.serializers import BookSerializer


class StoreSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only= False)

    class Meta:
        model = Store
        fields = ['id', 'name', 'books']
