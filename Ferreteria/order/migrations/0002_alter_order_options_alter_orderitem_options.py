# Generated by Django 5.1.2 on 2024-10-26 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created_at'], 'verbose_name': 'Información Ordenes', 'verbose_name_plural': 'Información de Órdenes'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Orden', 'verbose_name_plural': 'Órdenes'},
        ),
    ]
