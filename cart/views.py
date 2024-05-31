from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import Cart, BookQuantity
from .serializers import CartSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
