from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Order, OrderItem
from .return_books import return_books
from .serializers import OrderSerializer, CancelOrderSerializer
from cart.models import Cart, BookQuantity
from django.http import Http404


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            return Order.objects.filter(user=user)
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action == 'cancel_order':
            return CancelOrderSerializer

        return OrderSerializer

    def perform_create(self, serializer):
        confirmation = self.request.data.get('confirm_order', False)
        if not confirmation:
            return
        user = self.request.user
        try:
            cart = user.user_cart
            book_quantities = cart.book_quantity.all()
        except Cart.DoesNotExist:
            raise Http404("User does not have a cart")

        total_price = 0
        order = serializer.save(user=user)

        for book_quantity in book_quantities:
            book = book_quantity.book
            store = book_quantity.store
            quantity = book_quantity.quantity
            price = book.price

            total_price += price * quantity

            OrderItem.objects.create(
                order=order,
                book=book,
                store=store,
                quantity=quantity,
                price=price
            )

        order.total_amount = total_price
        order.save()

    @action(detail=False, methods=['patch'], url_path='cancel-order')
    def cancel_order(self, request, *args, **kwargs):
        data = self.request.data
        order_id = data.get('order_id')
        order = Order.objects.get(id=order_id)
        if order.user != self.request.user:
            return Response('Cannot perform', status=status.HTTP_400_BAD_REQUEST)
        if order.status == 'Cancelled':
            return Response('Already Cancelled', status=status.HTTP_400_BAD_REQUEST)
        order.status = 'Cancelled'
        order.save()
        return_books(order_id)
        return Response('cancelled the order')
