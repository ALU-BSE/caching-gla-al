from rest_framework import routers
from django.urls import path, include
from .views import UserViewSet

# DRF router for UserViewSet
router = routers.DefaultRouter()
router.register(r'', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]