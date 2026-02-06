from rest_framework import viewsets
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache
from django.conf import settings

from users.models import User
from users.serializers import UserSerializer

CACHE_TTL = getattr(settings, "CACHE_TTL", 60 * 5)  # Default 5 minutes

@method_decorator(cache_page(CACHE_TTL), name="list")
class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Users.
    - GET /users/ is cached for CACHE_TTL seconds.
    - Cache is invalidated automatically on create, update, or delete.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    CACHE_KEY = "all_users"

    def perform_create(self, serializer):
        """Save a new user and invalidate the cache."""
        serializer.save()
        cache.delete(self.CACHE_KEY)

    def perform_update(self, serializer):
        """Update a user and invalidate the cache."""
        serializer.save()
        cache.delete(self.CACHE_KEY)

    def perform_destroy(self, instance):
        """Delete a user and invalidate the cache."""
        instance.delete()
        cache.delete(self.CACHE_KEY)
