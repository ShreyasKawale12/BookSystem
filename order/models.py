from django.db import models

# Create your models here.
STATUS_CHOICES = [
    ('SUCCESS', 'Success'),
    ('FAILED', 'Failed'),
]


class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='SUCCESS')
    order_message = models.TextField(default= 'Order Created Successfully')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)

    def __str__(self):
        return f"Order #{self.id} by {self.user}"

