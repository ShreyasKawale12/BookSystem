from rest_framework import serializers
from .models import Book, Author, Publisher, Review


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'age', 'date_of_birth', 'date_of_death', 'nationality', 'photo']


class AuthorPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'date_of_birth', 'date_of_death', 'nationality', 'photo']


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer(read_only=False)
    # publisher = PublisherSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'publication_date', 'publisher', 'rating', 'price']


class ReviewSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['content', 'book']
