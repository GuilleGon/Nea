# Generated by Django 3.2.9 on 2021-12-11 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0003_auto_20211211_1326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='RazonSocial',
            new_name='razonSocial',
        ),
        migrations.RenameField(
            model_name='empresa',
            old_name='Rubro',
            new_name='rubro',
        ),
    ]
