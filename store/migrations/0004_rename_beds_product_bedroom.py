# Generated by Django 4.0.5 on 2022-07-22 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='beds',
            new_name='bedroom',
        ),
    ]
