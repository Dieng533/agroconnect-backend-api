import os
import django
from django.utils import timezone

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from products.models import AgriculturalAdvice

# Créer des conseils agricoles exemples
sample_advices = [
    {
        'title': 'Conseils pour la plantation de maïs',
        'content': 'Le maïs doit être planté à une profondeur de 2-3 cm dans un sol bien préparé. Espacement recommandé: 75cm entre les rangs et 25cm entre les plants. Assurez-vous que le sol soit bien drainé et riche en matière organique.',
        'advice_type': 'planting',
        'crop_type': 'cereals',
    },
    {
        'title': 'Fertilisation des légumes-feuilles',
        'content': 'Pour les légumes-feuilles comme les épinards et la laitue, utilisez un engrais riche en azote. Appliquez l\'engrais 3-4 semaines après la plantation. Évitez de sur-fertiliser pour ne pas brûler les racines.',
        'advice_type': 'fertilization',
        'crop_type': 'vegetables',
    },
    {
        'title': 'Lutte contre les pucerons',
        'content': 'Les pucerons peuvent être contrôlés naturellement avec des solutions de savon noir ou de l\'huile de neem. Pulvérisez le matin ou le soir pour éviter de brûler les feuilles. Encouragez les prédateurs naturels comme les coccinelles.',
        'advice_type': 'pest_control',
        'crop_type': 'vegetables',
    },
    {
        'title': 'Quand récolter les tomates',
        'content': 'Récoltez les tomates lorsqu\'elles sont bien colorées mais encore fermes au toucher. Ne les laissez pas trop mûrir sur la plante car elles peuvent devenir trop molles. Les récolter régulièrement encourage la production de nouveaux fruits.',
        'advice_type': 'harvesting',
        'crop_type': 'vegetables',
    },
    {
        'title': 'Conseils généraux pour l\'irrigation',
        'content': 'Arrosez vos cultures tôt le matin ou tard le soir pour réduire l\'évaporation. L\'arrosage profond et moins fréquent est préférable à des arrosages fréquents et superficiels. Vérifiez l\'humidité du sol avant d\'arroser.',
        'advice_type': 'general',
        'crop_type': 'other',
    },
    {
        'title': 'Plantation des tubercules (pommes de terre)',
        'content': 'Plantez les tubercules pré-germés à 10-15cm de profondeur avec les germes vers le haut. Espacement: 30cm entre les plants et 60cm entre les rangs. Buttez les plants lorsque les feuilles atteignent 20-25cm de hauteur.',
        'advice_type': 'planting',
        'crop_type': 'tubers',
    },
]

print("Création des conseils agricoles...")
for advice_data in sample_advices:
    advice, created = AgriculturalAdvice.objects.get_or_create(
        title=advice_data['title'],
        defaults=advice_data
    )
    if created:
        print(f"Créé: {advice.title}")
    else:
        print(f"Déjà existant: {advice.title}")

print(f"\nTotal des conseils dans la base: {AgriculturalAdvice.objects.count()}")
