# Generated by Django 3.1.13 on 2022-01-26 17:35

import timezone_field.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_auto_20210922_2349"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="timezone",
            field=timezone_field.fields.TimeZoneField(
                default="Asia/Kolkata",
                # America -> Asia
                help_text="Primary timezone for this user",
                verbose_name="User's Timezone",
            ),
        ),
    ]
