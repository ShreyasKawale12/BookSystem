# Generated by Django 3.2.25 on 2024-06-18 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('reason', models.TextField()),
                ('status', models.CharField(choices=[('PENDING', 'pending'), ('CNF', 'Confirmed'), ('FAIL', 'Failed')], max_length=7)),
                ('requested_at', models.DateTimeField(auto_now_add=True)),
                ('processed_at', models.DateTimeField()),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_refund', to='payment.payment')),
            ],
        ),
    ]
