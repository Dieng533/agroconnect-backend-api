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
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    location = models.CharField(max_length=255, help_text='Localisation du produit')
    farmer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'product']  # Un produit ne peut apparaître qu'une fois par utilisateur

    def __str__(self):
        return f"{self.user.email} - {self.product.name} ({self.quantity})"

    @property
    def total_price(self):
        return self.product.price * self.quantity

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="pending")
    image = models.ImageField(upload_to='orders/', null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.buyer}"

    @property
    def total_price(self):
        return self.product.price * self.quantity

class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"Message from {self.sender.email} to {self.receiver.email}"

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
        return f"{self.name} - {self.farmer.email}"

class AgriculturalAdvice(models.Model):
    ADVICE_TYPE_CHOICES = [
        ('planting', 'Plantation'),
        ('fertilization', 'Fertilisation'),
        ('pest_control', 'Lutte antiparasitaire'),
        ('harvesting', 'Récolte'),
        ('general', 'Conseils généraux'),
    ]
    
    title = models.CharField(max_length=255)
    content = models.TextField()
    advice_type = models.CharField(max_length=20, choices=ADVICE_TYPE_CHOICES, default='general')
    crop_type = models.CharField(max_length=20, choices=Product.CATEGORY_CHOICES, default='other')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title