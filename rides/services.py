def find_nearest_riders(latitude, longitude, radius_km=2):
    """
    Logic to filter Riders who are active and within a specific radius.
    (Note: In production, use GeoDjango/PostGIS for this).
    """
    from users.models import User
    # Filter only users who are marked as RIDERS
    available_riders = User.objects.filter(user_type='RIDER', is_active=True)
    
    # Placeholder for geospatial math
    return available_riders