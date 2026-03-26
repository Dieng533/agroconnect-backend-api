import os
import sys
import django

# Configuration Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from products.models import AgriculturalAdvice

# Supprimer les anciens conseils
AgriculturalAdvice.objects.all().delete()

# Créer des conseils de test
advices = [
    {
        'title': 'Conseils de plantation pour le riz',
        'content': 'Le riz se plante mieux dans les sols argileux et humides. Assurez-vous que le champ a une bonne rétention d eau. La profondeur de plantation doit être de 2-3 cm.',
        'advice_type': 'planting',
        'crop_type': 'cereals',
    },
    {
        'title': 'Fertilisation des tomates',
        'content': 'Les tomates ont besoin d un apport équilibré en azote, phosphore et potassium. Utilisez un engrais NPK 10-10-10 toutes les 3 semaines pendant la saison de croissance.',
        'advice_type': 'fertilization',
        'crop_type': 'vegetables',
    },
    {
        'title': 'Lutte contre les pucerons',
        'content': 'Les pucerons peuvent être contrôlés naturellement avec du savon insecticide ou en introduisant des prédateurs comme les coccinelles. Évitez les pesticides chimiques excessifs.',
        'advice_type': 'pest_control',
        'crop_type': 'vegetables',
    },
    {
        'title': 'Récolte des arachides',
        'content': 'Les arachides sont prêtes à être récoltées lorsque les feuilles jaunissent et que les gousses sont bien formées. Arrachez les plants entiers et laissez-les sécher pendant 2-3 semaines.',
        'advice_type': 'harvesting',
        'crop_type': 'legumes',
    },
    {
        'title': 'Culture des pommes de terre',
        'content': 'Plantez les tubercules germés à 10 cm de profondeur dans des sillons espacés de 60 cm. Buttagez les plants lorsqu ils atteignent 20 cm de hauteur.',
        'advice_type': 'planting',
        'crop_type': 'tubers',
    },
    {
        'title': 'Conseils généraux d irrigation',
        'content': 'Arrosez tôt le matin ou tard le soir pour réduire l évaporation. La plupart des cultures ont besoin de 2-3 cm d eau par semaine.',
        'advice_type': 'general',
        'crop_type': 'other',
    },
]

print("Création des conseils agricoles de test...")
for advice_data in advices:
    advice = AgriculturalAdvice.objects.create(**advice_data)
    print(f"✅ Créé: {advice.title}")

print(f"\n{len(advices)} conseils agricoles créés avec succès!")
