from django.db import models

class TransportOrder(models.Model):
    order_number = models.CharField(max_length=100, unique=True)
    customer_name = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return f"{self.order_number} - {self.customer_name}"


class Waypoint(models.Model):
    PICKUP = 'pickup'
    DELIVERY = 'delivery'
    WAYPOINT_TYPE_CHOICES = [
        (PICKUP, 'Pickup'),
        (DELIVERY, 'Delivery'),
    ]
    
    transport_order = models.ForeignKey(TransportOrder, related_name='waypoints', on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    waypoint_type = models.CharField(max_length=10, choices=WAYPOINT_TYPE_CHOICES)

    def __str__(self):
        return f"{self.location} ({self.waypoint_type})"
