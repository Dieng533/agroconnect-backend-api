from django.urls import path
from .views import ProductListCreateView, OrderCreateView
from .views import ProductListCreateView, OrderCreateView, OrderUpdateStatusView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='products'),
    path('orders/', OrderCreateView.as_view(), name='orders'),
    path('orders/<int:pk>/status/', OrderUpdateStatusView.as_view(), name='order-status'),
]