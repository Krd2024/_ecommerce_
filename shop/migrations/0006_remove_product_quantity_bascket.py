# Generated by Django 5.0.7 on 2024-09-30 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_quantity_bascket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity_bascket',
        ),
    ]