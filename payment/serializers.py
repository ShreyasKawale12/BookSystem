from rest_framework import serializers
from .models import Payment, Refund


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['user', 'order', 'amount', 'payment_method', 'status', 'transaction_id']
        read_only_fields = ['user', 'order', 'amount', 'status', 'transaction_id']


class RefundSerializer(serializers.ModelSerializer):
    payment_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Refund
        fields = ['payment_id', 'reason']
