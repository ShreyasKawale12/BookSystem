from rest_framework import serializers
from .models import Book, Author, Publisher, Reviews


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'age', 'date_of_birth', 'date_of_death', 'nationality', 'photo']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    publisher = PublisherSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'publication_date', 'publisher', 'rating', 'price']


class ReviewsSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = Reviews
        fields = ['content', 'book']
