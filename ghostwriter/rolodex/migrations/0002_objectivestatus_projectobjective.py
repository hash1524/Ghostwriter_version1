# Generated by Django 2.2.3 on 2019-08-27 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rolodex", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ObjectiveStatus",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "objective_status",
                    models.CharField(
                        help_text="Enter an objective status (e.g. Active, On Hold)",
                        max_length=100,
                        unique=True,
                        verbose_name="Objective Status",
                    ),
                ),
            ],
            options={
                "verbose_name": "Objective status",
                "verbose_name_plural": "Objective status",
                "ordering": ["objective_status"],
            },
        ),
        migrations.CreateModel(
            name="ProjectObjective",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "objective",
                    models.TextField(
                        blank=True,
                        help_text="Provide a concise objective",
                        null=True,
                        verbose_name="Objective",
                    ),
                ),
                (
                    "complete",
                    models.BooleanField(
                        default=False,
                        help_text="Mark the objective as complete",
                        verbose_name="Completed",
                    ),
                ),
                (
                    "deadline",
                    models.DateField(
                        help_text="Provide a deadline for this objective",
                        max_length=100,
                        verbose_name="Due Date",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="rolodex.Project"
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="rolodex.ObjectiveStatus"
                    ),
                ),
            ],
            options={
                "verbose_name": "Project objective",
                "verbose_name_plural": "Project objectives",
                "ordering": ["project", "complete", "objective"],
            },
        ),
    ]