from django.db import models
from django.conf import settings

class Ride(models.Model):
    class RideStatus(models.TextChoices):
        REQUESTED = 'REQUESTED', 'Requested'
        ACCEPTED = 'ACCEPTED', 'Accepted'
        IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
        COMPLETED = 'COMPLETED', 'Completed'
        CANCELLED = 'CANCELLED', 'Cancelled'

    passenger = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rides_requested')
    rider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='rides_driven')
    pickup_address = models.CharField(max_length=255)
    destination_address = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=RideStatus.choices, default=RideStatus.REQUESTED)
    fare = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ride {self.id} - {self.status}"