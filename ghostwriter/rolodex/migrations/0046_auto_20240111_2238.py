# Generated by Django 3.2.19 on 2024-01-11 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rolodex', '0045_timezone_triggers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientcontact',
            name='name',
            field=models.CharField(default='Default Name', help_text="Enter the contact's full name", max_length=255, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectcontact',
            name='name',
            field=models.CharField(default='Default Name', help_text="Enter the contact's full name", max_length=255, verbose_name='Name'),
            preserve_default=False,
        ),
    ]