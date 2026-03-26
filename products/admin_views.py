from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, Sum, Avg
from django.utils import timezone
from datetime import timedelta
from .models import Product, Order, Message, AgriculturalAdvice
from users.models import User

@staff_member_required
def admin_dashboard(request):
    """Vue principale du tableau de bord administrateur"""
    
    # Statistiques générales
    total_products = Product.objects.count()
    total_orders = Order.objects.count()
    total_users = User.objects.count()
    total_advice = AgriculturalAdvice.objects.count()
    
    # Données récentes (7 derniers jours)
    seven_days_ago = timezone.now() - timedelta(days=7)
    
    recent_products = Product.objects.filter(
        created_at__gte=seven_days_ago
    ).order_by('-created_at')[:5]
    
    recent_orders = Order.objects.filter(
        created_at__gte=seven_days_ago
    ).order_by('-created_at')[:5]
    
    recent_messages = Message.objects.filter(
        timestamp__gte=seven_days_ago
    ).order_by('-timestamp')[:5]
    
    context = {
        'total_products': total_products,
        'total_orders': total_orders,
        'total_users': total_users,
        'total_advice': total_advice,
        'recent_products': recent_products,
        'recent_orders': recent_orders,
        'recent_messages': recent_messages,
        'title': 'Tableau de bord',
    }
    
    return render(request, 'admin/index.html', context)
