from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets


# Create your views here.

def send_view(request):
    return HttpResponse('hello')
