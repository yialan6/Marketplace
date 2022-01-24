# Generated by Django 3.2.9 on 2022-01-17 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_remove_listings_bids'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='bids',
            field=models.ManyToManyField(blank=True, to='auctions.Bids'),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='items',
            field=models.ManyToManyField(blank=True, null=True, to='auctions.Listings'),
        ),
    ]
