from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import send_view, AuthorViewSet, BookViewSet, PublisherViewSet, message_send
router = DefaultRouter()
from django.urls import path
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'publishers', PublisherViewSet)

urlpatterns = [
    path('email/', message_send, name = 'email' ),
]

urlpatterns += router.urls