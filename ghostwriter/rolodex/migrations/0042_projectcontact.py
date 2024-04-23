# Generated by Django 3.2.19 on 2023-08-29 18:19

from django.db import migrations, models
import django.db.models.deletion
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ("rolodex", "0041_auto_20230110_2347"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjectContact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Enter the contact's full name",
                        max_length=255,
                        null=True,
                        verbose_name="Name",
                    ),
                ),
                (
                    "job_title",
                    models.CharField(
                        blank=True,
                        help_text="Enter the contact's job title or project role as you want it to appear in a report",
                        max_length=255,
                        null=True,
                        verbose_name="Title or Role",
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True,
                        help_text="Enter an email address for this contact",
                        max_length=255,
                        null=True,
                        verbose_name="Email",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        help_text="Enter a phone number for this contact",
                        max_length=50,
                        null=True,
                        verbose_name="Phone",
                    ),
                ),
                (
                    "timezone",
                    timezone_field.fields.TimeZoneField(
                        default="Asia/Kolkata",
                        # America -> Asia
                        help_text="The contact's timezone",
                        verbose_name="Timezone",
                    ),
                ),
                (
                    "note",
                    models.TextField(
                        blank=True,
                        help_text="Provide additional information about the contact",
                        null=True,
                        verbose_name="Client Note",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rolodex.project",
                    ),
                ),
            ],
            options={
                "verbose_name": "Project POC",
                "verbose_name_plural": "Project POCs",
                "ordering": ["project", "id"],
            },
        ),
    ]
