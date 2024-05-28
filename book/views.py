import django_filters
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Book, Author, Publisher
from .serializers import AuthorSerializer, BookSerializer, PublisherSerializer, AuthorPostSerializer
from datetime import datetime
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Create your views here.
class AuthorFilter(django_filters.FilterSet):
    age = django_filters.NumberFilter(field_name='age', lookup_expr='gt')

    class Meta:
        model = Author
        fields = ['age', ]


class BookFilter(django_filters.FilterSet):
    price_gt = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_lt = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    name = django_filters.CharFilter(field_name= 'title', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['price_gt', 'price_lt', 'name' ]


def send_view(request):
    return HttpResponse('hello')


class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_class = AuthorFilter

    def perform_create(self, serializer):
        data = self.request.data.copy()
        dob = datetime.strptime(data['date_of_birth'], '%Y-%m-%d')
        age = (datetime.now() - dob).days // 365
        serializer.validated_data['age'] = age
        serializer.save()

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['age']
    search_fields = ['name', ]


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filterset_class = BookFilter
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['price']


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
