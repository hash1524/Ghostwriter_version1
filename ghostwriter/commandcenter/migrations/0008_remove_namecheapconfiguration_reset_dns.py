# Generated by Django 3.0.10 on 2021-06-16 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commandcenter', '0007_auto_20210616_0340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='namecheapconfiguration',
            name='reset_dns',
        ),
    ]