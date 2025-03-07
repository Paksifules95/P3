# Generated by Django 4.2.19 on 2025-03-01 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TransportOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=100, unique=True)),
                ('customer_name', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Waypoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('waypoint_type', models.CharField(choices=[('pickup', 'Pickup'), ('delivery', 'Delivery')], max_length=10)),
                ('transport_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waypoints', to='logistics.transportorder')),
            ],
        ),
    ]
