# Generated by Django 4.1.2 on 2022-10-17 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0009_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='pathsvg',
            field=models.TextField(default=''),
        ),
    ]
