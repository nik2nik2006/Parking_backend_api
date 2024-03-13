from django.urls import path, include
from rest_framework import routers

from api.views import ParkingSpaceViewSet, SaleViewSet
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'parking', ParkingSpaceViewSet, basename='parking')
router.register(r'sale', SaleViewSet, basename='sale')
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
