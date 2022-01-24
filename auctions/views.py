from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *


def index(request):
    return render(request, "auctions/index.html", {
        'items': Listings.objects.filter(winner=None),
        'title': 'Active Listings',
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        Watchlist.objects.create(user=user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def listing(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            details = request.POST
            b = Bids.objects.create(buyer=request.user, amount=0)
            item = Listings.objects.create(item=details['title'], seller=request.user, description=details['description'], starting_bid=details['starting_bid'], bids=b, category=details['category'], photo=details['image'])
            return HttpResponseRedirect(reverse('item', args=(item.id, )))

    return render(request, "auctions/listing.html")


def item(request, item_id):
    error = False
    item = Listings.objects.get(id=item_id)
    user = User.objects.get(id=request.user.id)
    is_seller = True if item.seller == user else False
    if request.method == 'POST':
        if request.POST.get('watchlist'):
            watchlist = Watchlist.objects.get(user=user)
            watchlist.items.add(item)
        if request.POST.get('placebid'):
            bid = float(request.POST['place_bid'])
            print(bid, item.bids.amount)
            if bid > item.bids.amount and bid > item.starting_bid:
                item.bids.delete()
                b = Bids.objects.create(buyer=user, amount=bid)
                item.bids = b
                item.save()
            else:
                error = True
        if request.POST.get('end_listing'):
            item.winner = user
            item.save()

    return render(request, 'auctions/item.html', {
        'listing': item,
        'user': user,
        'error': error,
        'is_seller': is_seller,
        'winner': item.winner,
    })


def watchlist(request):
    user = User.objects.get(id=request.user.id)
    try:
        watchlist = Watchlist.objects.get(user=user)
        items = watchlist.items.all()
    except:
        items = []
    return render(request, 'auctions/index.html', {
        'title': 'Saved Items',
        'items': items,
        'user': user
    })

def category(request, category):
    if category == 'completed':
        items = Listings.objects.exclude(winner=None)
        return render(request, 'auctions/index.html', {
            'title': 'Finalized Sales',
            'items': items
        })
    else:
        items = Listings.objects.filter(category=category)
        return render(request, 'auctions/index.html', {
            'title': f'{category}',
            'items': items
        })

def user_listing(request):
    user = User.objects.get(id=request.user.id)
    items = Listings.objects.filter(seller=request.user)
    return render(request, 'auctions/index.html', {
    'title': f'Your listings',
    'items': items
})

def winnings(request):
    wins = Listings.objects.filter(winner=request.user)
    return render(request, 'auctions/index.html', {
        'title': "Your winnings",
        'items': wins
    })