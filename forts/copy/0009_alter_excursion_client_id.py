# Generated by Django 4.2.20 on 2025-04-10 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forts', '0008_excursion_client_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excursion',
            name='client_id',
            field=models.BigIntegerField(default=0),
        ),
    ]
