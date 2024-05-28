from rest_framework.routers import DefaultRouter
from .views import send_view, AuthorViewSet, BookViewSet, PublisherViewSet
router = DefaultRouter()
from django.urls import path
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'publishers', PublisherViewSet)

urlpatterns = [

]

urlpatterns += router.urls