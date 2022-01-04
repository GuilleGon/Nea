# Generated by Django 3.2.9 on 2021-12-11 16:26

import Core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_auto_20211211_1204'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', Core.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='codigoPostal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='cuit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='domicilio',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]