from rest_framework.routers import DefaultRouter
from .views import StoreViewSet

router = DefaultRouter()

router.register(r'stores', StoreViewSet)

urlpatterns = list()

urlpatterns += router.urls