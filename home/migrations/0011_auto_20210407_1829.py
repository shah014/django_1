# Generated by Django 3.1.7 on 2021-04-07 18:29

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20210401_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.PositiveIntegerField(validators=[home.models.validate_my_age]),
        ),
    ]