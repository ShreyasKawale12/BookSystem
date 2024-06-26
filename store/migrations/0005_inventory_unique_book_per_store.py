# Generated by Django 3.2.25 on 2024-05-30 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_inventory_store'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='inventory',
            constraint=models.UniqueConstraint(fields=('store', 'book'), name='unique_book_per_store'),
        ),
    ]
