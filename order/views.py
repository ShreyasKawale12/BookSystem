from rest_framework import viewsets, permissions
from .models import Order, OrderItem
from .serializers import OrderSerializer
from cart.serializers import BookQuantitySerializer
from cart.models import Cart, BookQuantity
from django.http import Http404


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)

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
