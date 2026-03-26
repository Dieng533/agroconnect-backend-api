from django.contrib import admin
from .models import Product, Order, Cart, Message, AgriculturalAdvice, Culture

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'farmer', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description', 'farmer__username')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Informations générales', {
            'fields': ('name', 'description', 'category', 'price', 'quantity')
        }),
        ('Images', {
            'fields': ('image',)
        }),
        ('Agriculteur', {
            'fields': ('farmer',)
        }),
        ('Métadonnées', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer', 'product', 'quantity', 'order_date', 'status')
    list_filter = ('status', 'order_date')
    search_fields = ('buyer__username', 'id', 'product__name')
    readonly_fields = ('order_date',)
    ordering = ('-order_date',)
    
    fieldsets = (
        ('Informations commande', {
            'fields': ('buyer', 'product', 'quantity', 'status', 'image')
        }),
        ('Métadonnées', {
            'fields': ('order_date',),
            'classes': ('collapse',)
        }),
    )

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_at')
    search_fields = ('user__username', 'product__name')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'content_preview', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('sender__username', 'receiver__username', 'content')
    readonly_fields = ('timestamp',)
    ordering = ('-timestamp',)
    
    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Contenu'

@admin.register(AgriculturalAdvice)
class AgriculturalAdviceAdmin(admin.ModelAdmin):
    list_display = ('title', 'advice_type', 'crop_type', 'created_at')
    list_filter = ('advice_type', 'crop_type', 'created_at')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Informations conseil', {
            'fields': ('title', 'content', 'advice_type', 'crop_type')
        }),
        ('Métadonnées', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

@admin.register(Culture)
class CultureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at',)
    ordering = ('name',)

# Personnaliser l'interface admin
admin.site.site_header = "Administration AgroConnect"
admin.site.site_title = "AgroConnect Admin"
admin.site.index_title = "Bienvenue dans l'administration AgroConnect"
