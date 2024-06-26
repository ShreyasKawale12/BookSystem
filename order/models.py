from django.db import models
from django.contrib.auth.models import User
from book.models import Book
from store.models import Store

STATUS_CHOICES = [
    ('PENDING', 'Pending'),
    ('CONFIRMED', 'Confirmed'),
    ('PROCESSING', 'Processing'),
    ('SHIPPED', 'Shipped'),
    ('OUT_FOR_DELIVERY', 'Out for Delivery'),
    ('DELIVERED', 'Delivered'),
    ('CANCELLED', 'Cancelled'),
    ('FAILED', 'Failed'),
]


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Order #{self.id} by {self.user}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    out_for_delivery = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.book.title} from {self.store.name} in Order #{self.order.id}"
