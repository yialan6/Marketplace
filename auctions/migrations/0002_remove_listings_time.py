# Generated by Django 3.2.9 on 2022-01-09 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listings',
            name='time',
        ),
    ]
