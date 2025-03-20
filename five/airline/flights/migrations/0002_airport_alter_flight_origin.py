# Generated by Django 5.1.4 on 2025-01-13 17:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flights", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Airport",
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
                ("code", models.CharField(max_length=3)),
                ("city", models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name="flight",
            name="origin",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="departures",
                to="flights.airport",
            ),
        ),
    ]
