# Generated migration for AgroConnect

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_order_order_date_cart'),
    ]

    operations = [
        # Add new fields to Product model
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('cereals', 'Céréales'), ('vegetables', 'Légumes'), ('fruits', 'Fruits'), ('legumes', 'Légumineuses'), ('tubers', 'Tubercules'), ('other', 'Autres')], default='other', max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.CharField(default='', help_text='Localisation du produit', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        
        # Create Message model
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='users.user')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to='users.user')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        
        # Create Culture model
        migrations.CreateModel(
            name='Culture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('crop_type', models.CharField(choices=[('cereals', 'Céréales'), ('vegetables', 'Légumes'), ('fruits', 'Fruits'), ('legumes', 'Légumineuses'), ('tubers', 'Tubercules'), ('other', 'Autres')], default='other', max_length=20)),
                ('planting_date', models.DateField()),
                ('expected_harvest', models.DateField(blank=True, null=True)),
                ('area', models.DecimalField(decimal_places=2, help_text='Superficie en hectares', max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
        
        # Create AgriculturalAdvice model
        migrations.CreateModel(
            name='AgriculturalAdvice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('advice_type', models.CharField(choices=[('planting', 'Plantation'), ('fertilization', 'Fertilisation'), ('pest_control', 'Lutte antiparasitaire'), ('harvesting', 'Récolte'), ('general', 'Conseils généraux')], default='general', max_length=20)),
                ('crop_type', models.CharField(choices=[('cereals', 'Céréales'), ('vegetables', 'Légumes'), ('fruits', 'Fruits'), ('legumes', 'Légumineuses'), ('tubers', 'Tubercules'), ('other', 'Autres')], default='other', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
