# Generated by Django 3.2.9 on 2022-01-17 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_alter_listings_bids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='bids',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.bids'),
        ),
    ]
