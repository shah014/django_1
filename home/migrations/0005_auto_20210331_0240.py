# Generated by Django 3.1.7 on 2021-03-31 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210331_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='v_detail',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.vehicles'),
        ),
    ]
