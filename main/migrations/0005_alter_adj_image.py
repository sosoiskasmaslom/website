# Generated by Django 5.1.7 on 2025-04-03 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_adj_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adj',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='forts/static/adj/'),
        ),
    ]
