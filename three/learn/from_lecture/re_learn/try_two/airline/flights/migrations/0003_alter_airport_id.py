# Generated by Django 5.1.4 on 2025-01-21 01:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flights", "0002_airport_alter_flight_destination_alter_flight_origin"),
    ]

    operations = [
        migrations.AlterField(
            model_name="airport",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
