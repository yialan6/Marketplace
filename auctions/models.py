from django.contrib.auth.models import AbstractUser
from django.db import models
from django import utils

class User(AbstractUser):
    pass

class Bids(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.FloatField()


class Comments(models.Model):
    comment = models.CharField(max_length=100)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)


class Listings(models.Model):
    item = models.CharField(max_length=64, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='all_listings')
    bids = models.ForeignKey(Bids, on_delete=models.CASCADE, blank=True, null=True)
    starting_bid = models.FloatField(blank=False)
    category = models.CharField(max_length=20, default='All', blank=False)
    comments = models.ManyToManyField(Comments, blank=True)
    photo = models.URLField(blank=True)
    time = models.DateTimeField(blank=True, default=utils.timezone.now)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='listings_won')


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Listings, blank=True)
    
