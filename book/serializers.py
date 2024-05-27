from rest_framework import serializers
from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.SlugRelatedField(slug_field='name', queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ['title', 'author_name', 'genre', 'price']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'age', 'nationality']
