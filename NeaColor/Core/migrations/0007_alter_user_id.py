# Generated by Django 3.2.9 on 2022-01-27 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0006_alter_user_cuit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]