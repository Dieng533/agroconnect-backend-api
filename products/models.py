from django.db import models
from django.conf import settings

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('cereals', 'Céréales'),
        ('vegetables', 'Légumes'),
        ('fruits', 'Fruits'),
        ('legumes', 'Légumineuses'),
        ('tubers', 'Tubercules'),
        ('other', 'Autres'),
    ]
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    # Temporairement désactivé pour éviter Pillow
    image = models.CharField(max_length=500, null=True, blank=True, help_text="URL de l'image")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    location = models.CharField(max_length=255, help_text='Localisation du produit')
    farmer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('confirmed', 'Confirmée'),
        ('processing', 'En traitement'),
        ('shipped', 'Expédiée'),
        ('delivered', 'Livrée'),
        ('cancelled', 'Annulée'),
    ]
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="pending")
    # Temporairement désactivé pour éviter Pillow
    image = models.CharField(max_length=500, null=True, blank=True, help_text="URL de l'image")
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande #{self.id} par {self.buyer}"

    @property
    def total_price(self):
        return self.product.price * self.quantity

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Panier de {self.user} - {self.product.name}"

class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message de {self.sender} à {self.receiver}"

class AgriculturalAdvice(models.Model):
    ADVICE_TYPE_CHOICES = [
        ('planting', 'Plantation'),
        ('fertilization', 'Fertilisation'),
        ('harvesting', 'Récolte'),
        ('protection', 'Protection des cultures'),
        ('irrigation', 'Irrigation'),
        ('other', 'Autres'),
    ]
    CROP_TYPE_CHOICES = [
        ('cereals', 'Céréales'),
        ('vegetables', 'Légumes'),
        ('fruits', 'Fruits'),
        ('tubers', 'Tubercules'),
        ('other', 'Autres'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    advice_type = models.CharField(max_length=20, choices=ADVICE_TYPE_CHOICES, default='other')
    crop_type = models.CharField(max_length=20, choices=CROP_TYPE_CHOICES, default='other')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Culture(models.Model):
    CROP_TYPE_CHOICES = [
        ('cereals', 'Céréales'),
        ('vegetables', 'Légumes'),
        ('fruits', 'Fruits'),
        ('legumes', 'Légumineuses'),
        ('tubers', 'Tubercules'),
        ('other', 'Autres'),
    ]
    
    farmer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    crop_type = models.CharField(max_length=20, choices=CROP_TYPE_CHOICES, default='other')
    planting_date = models.DateField()
    expected_harvest = models.DateField(null=True, blank=True)
    area = models.DecimalField(max_digits=10, decimal_places=2, help_text='Superficie en hectares')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.farmer.username}"
