# Generated by Django 3.2.19 on 2023-06-15 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='enable_finding_create',
            field=models.BooleanField(default=False, help_text='Allow the user to create new findings (only applies to account with the User role)', verbose_name='Enable Finding Creation'),
        ),
        migrations.AddField(
            model_name='user',
            name='enable_finding_edit',
            field=models.BooleanField(default=False, help_text='Allow the user to edit existing findings (only applies to accounts with the User role)', verbose_name='Enable Finding Editing'),
        ),
    ]
