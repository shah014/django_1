# Generated by Django 3.1.7 on 2021-03-30 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('cost', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('v_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.vehicles')),
            ],
        ),
    ]
