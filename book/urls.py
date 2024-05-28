from rest_framework.routers import DefaultRouter
from .views import send_view, AuthorView, BookView, PublisherViewSet
router = DefaultRouter()
from django.urls import path
router.register(r'authors', AuthorView)
router.register(r'books', BookView)
router.register(r'publishers', PublisherViewSet)

urlpatterns = [

]

urlpatterns += router.urls