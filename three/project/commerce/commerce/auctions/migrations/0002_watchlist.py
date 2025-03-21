# Generated by Django 5.1.4 on 2025-02-05 12:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Watchlist",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "watchlist_listing",
                    models.ManyToManyField(
                        related_name="watchlist_item", to="auctions.auction_listing"
                    ),
                ),
                (
                    "watchlist_username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="watchlist_username",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
