# Generated by Django 4.0.5 on 2022-07-20 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_rented_product_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default='0'),
        ),
    ]
