# Generated by Django 4.1.2 on 2022-10-20 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0014_remove_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
