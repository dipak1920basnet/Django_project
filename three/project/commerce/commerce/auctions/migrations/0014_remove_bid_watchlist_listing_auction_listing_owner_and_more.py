# Generated by Django 5.1.4 on 2025-02-08 07:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0013_remove_auction_listing_owner"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bid",
            name="Watchlist_listing",
        ),
        migrations.AddField(
            model_name="auction_listing",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="auction_listing",
            name="watchlist",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="onwatchlist",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.DeleteModel(
            name="Watchlist",
        ),
    ]
