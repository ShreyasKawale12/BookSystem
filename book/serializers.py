from rest_framework import serializers
from .models import Book, Author, Publisher, Review, Distribution
from datetime import date


class DistributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distribution
        fields = ['store', 'user', 'quantity']


class AuthorNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    author_details = AuthorNestedSerializer(source='author', read_only=True)
    book_distribution = DistributionSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['title', 'author', 'author_details','book_distribution', 'genre', 'publication_date', 'publisher',
                  'rating', 'price']


class PublisherSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Publisher
        fields = ['id', 'name', 'books', ]


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    age = serializers.SerializerMethodField()

    def get_age(self, obj):
        if obj.date_of_birth:
            today = date.today()
            dob = obj.date_of_birth
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            return age
        return None

    class Meta:
        model = Author
        fields = ['name', 'user', 'books', 'age', 'date_of_birth', 'date_of_death', 'nationality', 'photo']


class AuthorPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'date_of_birth', 'date_of_death', 'nationality', 'photo']


class ReviewSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['content', 'book']
