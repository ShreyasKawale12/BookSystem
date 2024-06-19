from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet

router = DefaultRouter()

router.register('payments', PaymentViewSet)

urlpatterns = list()

urlpatterns += router.urls
