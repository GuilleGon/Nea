# Generated by Django 3.2.9 on 2022-01-08 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0005_user_is_email_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cuit',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]