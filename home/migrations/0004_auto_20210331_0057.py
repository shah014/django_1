# Generated by Django 3.1.7 on 2021-03-31 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_driver_vehicles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='v_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_drivers', to='home.vehicles'),
        ),
    ]
