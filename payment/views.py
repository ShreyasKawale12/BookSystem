from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Payment
from .serializers import PaymentSerializer, RefundSerializer
import uuid


# Create your views here.

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get_serializer_class(self):
        if self.action == 'refund_order':
            return RefundSerializer
        return super().get_serializer_class()
    def perform_create(self, serializer):
        user = self.request.user
        data = self.request.data
        order = user.orders.latest('created_at')
        amount = order.total_amount
        payment = serializer.save(user=user, order=order, amount=amount, status='PENDING', transaction_id=uuid.uuid4())

    @action(detail=False, methods=['patch',], url_path='refund')
    def refund_order(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        refund = serializer.save()

