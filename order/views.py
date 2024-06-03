from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Order
from .serializers import OrderSerializer


# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            return Order.objects.filter(user=user)
        return super().get_queryset()

    def perform_create(self, serializer):
        user = serializer.validated_data.get('user')
        try:
            cart = user.user_cart
            book_quantities = cart.book_quantity.all()
        except Exception:
            raise Http404("User does not have a cart")
        total_price = 0
        for book_quantity in book_quantities:
            book_price = book_quantity.book.price
            quantity = book_quantity.quantity
            total_price += book_price * quantity

        serializer.save(total_amount=total_price)

    permission_classes = [permissions.IsAuthenticated]
