from rest_framework.routers import DefaultRouter
router = DefaultRouter()
from .views import CartViewSet
router.register(r'carts', CartViewSet)

urlpatterns = list()

urlpatterns += router.urls