# Generated by Django 3.2 on 2022-08-09 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_discounted_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discount_percent',
        ),
        migrations.RemoveField(
            model_name='product',
            name='discounted_price',
        ),
    ]
