from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Store
from .serializers import StoreSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
