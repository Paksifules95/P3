from django.urls import path
from .views import TransportOrderListCreateView

urlpatterns = [
    path('orders/', TransportOrderListCreateView.as_view(), name='orders-list-create'),
]
