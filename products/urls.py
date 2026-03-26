from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . import admin_views
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'farmers', views.FarmerViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'cart', views.CartViewSet)
router.register(r'messages', views.MessageViewSet)
router.register(r'cultures', views.CultureViewSet)
router.register(r'advice', views.AgriculturalAdviceViewSet, basename='agricultural-advice')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/products/<int:product_id>/', views.ProductDetailView.as_view()),
    path('api/farmers/<int:farmer_id>/', views.FarmerDetailView.as_view()),
    path('api/orders/<int:order_id>/', views.OrderDetailView.as_view()),
    path('api/messages/<int:message_id>/', views.MessageDetailView.as_view()),
    path('api/cultures/<int:culture_id>/', views.CultureDetailView.as_view()),
    path('api/advice/<int:advice_id>/', views.AgriculturalAdviceDetailView.as_view()),
    path('api/advice/create/', views.AgriculturalAdviceCreateView.as_view()),
    
    # URLs d'administration personnalisées
    path('admin/dashboard/', admin_views.admin_dashboard, name='admin_dashboard'),
    
    # URLs d'authentification
    path('admin/login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='admin_login'),
    path('admin/logout/', auth_views.LogoutView.as_view(next_page='admin:index'), name='admin_logout'),

    # Messages
    path('messages/', MessageListView.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),
    path('messages/conversation/<int:user_id>/', ConversationView.as_view(), name='conversation'),

    # Cultures
    path('cultures/', CultureListCreateView.as_view(), name='culture-list-create'),
    path('cultures/<int:pk>/', CultureDetailView.as_view(), name='culture-detail'),

    # Agricultural Advice
    path('advice/', AgriculturalAdviceListView.as_view(), name='advice-list'),
    path('advice/create/', AgriculturalAdviceCreateView.as_view(), name='advice-create'),
    path('advice/<int:pk>/', AgriculturalAdviceDetailView.as_view(), name='advice-detail'),
]