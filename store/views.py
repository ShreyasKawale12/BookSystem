from django.shortcuts import render
from rest_framework import viewsets, permissions
# Create your views here.
from .models import Store
from .serializers import StoreSerializer
from .permissions import IsSuperUser


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]