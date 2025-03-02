from rest_framework import generics
from .models import TransportOrder
from .serializers import TransportOrderSerializer

class TransportOrderListCreateView(generics.ListCreateAPIView):
    queryset = TransportOrder.objects.all()
    serializer_class = TransportOrderSerializer
