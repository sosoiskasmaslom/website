# Generated by Django 4.2.20 on 2025-04-14 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_alter_user_first_name_alter_user_last_name_and_more'),
        ('forts', '0014_remove_excursion_client_excursion_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excursion',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.user'),
        ),
    ]
