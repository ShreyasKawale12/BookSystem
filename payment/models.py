from django.db import models

# Create your models here.

payment_choices = [
    ('UPI', 'Upi Payment'),
    ('COD', 'Cash on Delivery'),
    ('DEBIT', 'Debit Card'),
    ('CREDIT', 'Credit Card'),
]

status_choices = [
    ('PENDING', 'pending'),
    ('CNF', 'Confirmed'),
    ('FAIL', 'Failed')
]


class Payment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='user_payment')
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE, related_name='order_payment')
    amount = models.FloatField(default=0)
    payment_method = models.CharField(max_length=6, choices=payment_choices)
    status = models.CharField(max_length=7, choices=status_choices)
    transaction_id = models.CharField(max_length= 50)
    created_at = models.DateTimeField(auto_now_add=True)


class Refund(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='payment_refund')
    amount = models.FloatField(default=0)
    reason = models.TextField()
    status = models.CharField(max_length=7, choices=status_choices)
    requested_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField()


class TransactionLog(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=7, choices=status_choices)
    logged_at = models.DateTimeField()





