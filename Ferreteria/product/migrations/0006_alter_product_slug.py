# Generated by Django 5.1.2 on 2024-10-27 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_category_slug_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(verbose_name='Nombre sin espacios y en minusculas para url'),
        ),
    ]
