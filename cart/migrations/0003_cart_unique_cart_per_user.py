# Generated by Django 3.2.25 on 2024-05-31 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20240531_0848'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='cart',
            constraint=models.UniqueConstraint(fields=('user',), name='unique_cart_per_user'),
        ),
    ]
