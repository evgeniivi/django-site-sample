# Generated by Django 4.1.2 on 2022-10-14 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0004_alter_ufoslide_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='menuitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=25)),
                ('color', models.CharField(max_length=6)),
            ],
        ),
    ]
