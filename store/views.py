from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
from .models import Store
from .serializers import StoreSerializer
from .permissions import IsSuperUser


class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]

    def get_queryset(self):
        owner = self.request.user
        qs = Store.objects.all()
        if not owner.is_superuser:
            return qs.filter(owner=owner)
        return qs

    @action(detail=False, methods=['patch'], url_path='send-goods')
    def send_goods(self, request, *args, **kwargs):
        store = Store.objects.get(owner=self.request.user)
        serializer = self.get_serializer(store, data=request.data, partial=True )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

