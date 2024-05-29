# Generated by Django 3.2.25 on 2024-05-29 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0006_delete_store'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('books', models.ManyToManyField(related_name='books', to='book.Book')),
            ],
        ),
    ]
