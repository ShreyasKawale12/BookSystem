from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email_task(subject, message, from_email, recipient_list):
    send_mail(subject, message, from_email, recipient_list)


@shared_task
def send_message():
    return "Hello World"


@shared_task
def add(a, b):
    return a + b


@shared_task
def multiply(a, b):
    return a * b


@shared_task
def subtract(a, b):
    return a - b


@shared_task
def divide(a, b):
    return a / b


@shared_task
def immutable_task():
    return "immutable task"


@shared_task
def divide(a, b):
    return a / b


@shared_task
def error_handler(request, exc, traceback):
    print(f"Task id = {request.id} failed: {exc}\n{traceback}")
