# Generated by Django 4.1.4 on 2023-02-25 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='images',
            new_name='image',
        ),
    ]