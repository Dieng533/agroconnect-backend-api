from django.urls import path
from .views import (
    ProductListCreateView, ProductDetailView, OrderListCreateView, OrderDetailView,
    BulkOrderCreateView, CartListView, CartDetailView, CartClearView, FarmerListView,
    MessageListView, MessageDetailView, ConversationView,
    CultureListCreateView, CultureDetailView,
    AgriculturalAdviceListView, AgriculturalAdviceDetailView
)

urlpatterns = [
    # Products
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    # Orders
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/bulk/', BulkOrderCreateView.as_view(), name='bulk-order-create'),

    # Cart
    path('cart/', CartListView.as_view(), name='cart-list-create'),
    path('cart/<int:pk>/', CartDetailView.as_view(), name='cart-detail'),
    path('cart/clear/', CartClearView.as_view(), name='cart-clear'),

    # Farmers
    path('farmers/', FarmerListView.as_view(), name='farmer-list'),

    # Messages
    path('messages/', MessageListView.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),
    path('messages/conversation/<int:user_id>/', ConversationView.as_view(), name='conversation'),

    # Cultures
    path('cultures/', CultureListCreateView.as_view(), name='culture-list-create'),
    path('cultures/<int:pk>/', CultureDetailView.as_view(), name='culture-detail'),

    # Agricultural Advice
    path('advice/', AgriculturalAdviceListView.as_view(), name='advice-list'),
    path('advice/<int:pk>/', AgriculturalAdviceDetailView.as_view(), name='advice-detail'),
]