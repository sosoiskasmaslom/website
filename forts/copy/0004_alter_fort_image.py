# Generated by Django 5.1.7 on 2025-04-02 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forts', '0003_excursion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fort',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
