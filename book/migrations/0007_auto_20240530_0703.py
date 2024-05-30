# Generated by Django 3.2.25 on 2024-05-30 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_inventory_unique_book_per_store'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0006_delete_store'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_distribution', to='book.book')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.store')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_book_distribution', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='users',
            field=models.ManyToManyField(related_name='books', through='book.Distribution', to=settings.AUTH_USER_MODEL),
        ),
    ]