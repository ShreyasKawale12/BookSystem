from rest_framework.routers import DefaultRouter
router = DefaultRouter()
from .views import CartViewSet, CartItemViewSet
router.register(r'carts', CartViewSet)
router.register(r'cart_items', CartItemViewSet)

urlpatterns = list()

urlpatterns += router.urls