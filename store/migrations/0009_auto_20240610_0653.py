# Generated by Django 3.2.25 on 2024-06-10 06:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0008_remove_store_revenue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='customers',
        ),
        migrations.AddField(
            model_name='store',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
