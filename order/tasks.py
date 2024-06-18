from celery import shared_task
from order.models import Order
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum
from django.core.mail import send_mail


@shared_task
def revenue_per_five_minutes():
    five_minutes_ago = timezone.now() - timedelta(minutes=5)
    revenue = Order.objects.filter(created_at__gte=five_minutes_ago).aggregate(revenue=Sum('total_amount'))
    subject = 'Revenue of 5 minutes'
    message = f'''
        The revenue generated last 5 minutes is {revenue.get('revenue') or 0} Rupees 
    '''
    from_email = 'shreyaskawale7t@gmail.com'
    recipient_list = ['kawaleshreyas33@gmail.com',]
    send_mail(subject, message, from_email, recipient_list)

