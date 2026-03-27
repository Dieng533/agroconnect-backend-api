from django.urls import path, include
from . import views
from . import admin_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # API URLs
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    
    path('orders/', views.OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    
    path('cart/', views.CartListView.as_view(), name='cart-list'),
    path('cart/<int:pk>/', views.CartDetailView.as_view(), name='cart-detail'),
    path('cart/clear/', views.CartClearView.as_view(), name='cart-clear'),
    
    path('farmers/', views.FarmerListView.as_view(), name='farmer-list'),
    
    path('messages/', views.MessageListView.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', views.MessageDetailView.as_view(), name='message-detail'),
    path('messages/conversation/<int:user_id>/', views.ConversationView.as_view(), name='conversation'),
    
    path('cultures/', views.CultureListCreateView.as_view(), name='culture-list-create'),
    path('cultures/<int:pk>/', views.CultureDetailView.as_view(), name='culture-detail'),
    
    path('advice/', views.AgriculturalAdviceListView.as_view(), name='advice-list'),
    path('advice/<int:pk>/', views.AgriculturalAdviceDetailView.as_view(), name='advice-detail'),
    path('advice/create/', views.AgriculturalAdviceCreateView.as_view(), name='advice-create'),
    
    # URLs d'administration personnalisées
    path('admin/dashboard/', admin_views.admin_dashboard, name='admin_dashboard'),
    
    # URLs d'authentification
    path('admin/login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='admin_login'),
    path('admin/logout/', auth_views.LogoutView.as_view(next_page='admin:index'), name='admin_logout'),
]