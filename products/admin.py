from django.contrib import admin
from .models import Product, Order, Cart, CartItem, Message, AgriculturalAdvice, Culture

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'farmer', 'created_at', 'is_available')
    list_filter = ('category', 'is_available', 'created_at')
    search_fields = ('name', 'description', 'farmer__username')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Informations générales', {
            'fields': ('name', 'description', 'category', 'price', 'quantity', 'is_available')
        }),
        ('Images', {
            'fields': ('image',)
        }),
        ('Agriculteur', {
            'fields': ('farmer',)
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer', 'created_at', 'total_amount', 'status')
    list_filter = ('status', 'created_at')
    search_fields = ('buyer__username', 'id')
    readonly_fields = ('created_at', 'updated_at', 'total_amount')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Informations commande', {
            'fields': ('buyer', 'status')
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at', 'total_amount'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'created_at')
    search_fields = ('buyer__username',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'added_at')
    list_filter = ('added_at',)
    search_fields = ('product__name', 'cart__buyer__username')
    readonly_fields = ('added_at',)
    ordering = ('-added_at',)

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
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Informations conseil', {
            'fields': ('title', 'content', 'advice_type', 'crop_type')
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Culture)
class CultureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('name',)

# Personnaliser l'interface admin
admin.site.site_header = "Administration AgroConnect"
admin.site.site_title = "AgroConnect Admin"
admin.site.index_title = "Bienvenue dans l'administration AgroConnect"
