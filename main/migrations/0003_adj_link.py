# Generated by Django 5.1.7 on 2025-04-03 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_fort_adj'),
    ]

    operations = [
        migrations.AddField(
            model_name='adj',
            name='link',
            field=models.CharField(default='', max_length=250),
        ),
    ]
