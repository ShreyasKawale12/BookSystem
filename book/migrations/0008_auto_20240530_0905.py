# Generated by Django 3.2.25 on 2024-05-30 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20240530_0703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='users',
        ),
        migrations.DeleteModel(
            name='Distribution',
        ),
    ]
