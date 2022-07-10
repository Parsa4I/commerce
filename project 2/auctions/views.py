from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required
from .models import *


class BidForm(forms.Form):
    bid = forms.IntegerField(label='Your Bid')


category_choices = {
    'ELC': 'Electronics',
    'BMM': 'Books, Movies & Music',
    'ART': 'Art',
    'FSH': 'Fashion',
    'THB': 'Toys and Hobbies',
    'SPG': 'Sporting Goods',
    'HBT': 'Health & Beauty',
    'BZI': 'Business & Industrial',
    'HMG': 'Home & Garden',
    'ACS': 'Accessories',
    'JWR': 'Jewerly',
    'OTR': 'Other'
}


def index(request):
    items = Item.objects.filter(is_sold=False)
    return render(request, "auctions/index.html", {
        'items': items
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
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def item(request, item_id):
    itm = Item.objects.get(id=item_id)
    user = request.user
    watchlistmsg = ''
    your_bid = ''
    comments = Comment.objects.filter(item_id=itm.id)

    is_watched = True
    try:
        watched = Watchlist_Item.objects.get(item=itm, user=user)
    except:
        is_watched = False

    if not user.is_anonymous:
        if is_watched:
            watchlistmsg = 'Remove from watchlist'
        else:
            watchlistmsg = 'Add to watchlist'
    if user == itm.high_bid_user:
        if itm.is_sold:
            your_bid = 'Congratulations! The auction ended and your bid was the highest one. This item is yours now!'
        else:
            your_bid = 'Your bid is the current bid.'

    if request.method == 'POST':
        if 'place_bid' in request.POST:
            bid = int(request.POST['bid'])
            new_bid = Bid(user=user, amount=request.POST['bid'], item=itm)
            if itm.high_bid is not None:
                if bid > itm.high_bid:
                    itm.high_bid = bid
                    itm.high_bid_user = user
                    itm.bid_number += 1
                    itm.save()
                    new_bid.save()
                    bidform = BidForm()
                    return HttpResponseRedirect(f'{itm.id}')
                else:
                    bidform = BidForm(request.POST)
                    return render(request, 'auctions/item.html', {
                        'item': itm,
                        'bidform': bidform,
                        'bidnum': itm.bid_number,
                        'warning': 'Your bid should be more than the high bid.',
                        'your_bid': your_bid,
                        'is_watched': is_watched,
                        'watchlistmsg': watchlistmsg,
                        'category': category_choices[itm.category],
                        'seller': itm.seller,
                        'comments': comments
                    })
            elif bid >= itm.starting_bid:
                itm.high_bid = bid
                itm.high_bid_user = user
                itm.bid_number += 1
                itm.save()
                new_bid.save()
                bidform = BidForm()
                return HttpResponseRedirect(f'{itm.id}')
            else:
                bidform = BidForm(request.POST)
                return render(request, 'auctions/item.html', {
                    'item': itm,
                    'bidform': bidform,
                    'bidnum': itm.bid_number,
                    'warning': 'Your bid should be more than the high bid.',
                    'your_bid': your_bid,
                    'is_watched': is_watched,
                    'watchlistmsg': watchlistmsg,
                    'category': category_choices[itm.category],
                    'seller': itm.seller,
                    'comments': comments
                })
        elif 'end_auction' in request.POST:
            itm.is_sold = True
            itm.save()
            return HttpResponseRedirect(reverse('index'))
        elif 'comment' in request.POST:
            comment = Comment(
                user=user, comment_text=request.POST['comment-txt'], item=itm)
            comment.save()
            return HttpResponseRedirect(f'{itm.id}')
    else:
        bidform = BidForm()
        return render(request, 'auctions/item.html', {
            'item': itm,
            'bidform': bidform,
            'bidnum': itm.bid_number,
            'your_bid': your_bid,
            'is_watched': is_watched,
            'watchlistmsg': watchlistmsg,
            'category': category_choices[itm.category],
            'seller': itm.seller,
            'comments': comments
        })


@login_required(login_url='login')
def create_listing(request):
    if request.method == 'POST':
        itm_title = request.POST['title']
        itm_summary = request.POST['summary']
        itm_category = request.POST['category']
        itm_description = request.POST['description']
        itm_picurl = request.POST['picture']
        if itm_picurl == '':
            itm_picurl = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/2048px-No_image_available.svg.png'
        itm_starting_bid = request.POST['starting-bid']
        itm = Item(
            title=itm_title,
            summary=itm_summary,
            category=itm_category,
            description=itm_description,
            image=itm_picurl,
            starting_bid=itm_starting_bid,
            seller=request.user
        )
        itm.save()
        return HttpResponseRedirect(f'item/{itm.id}')

    categories = list(Item.CATEGORY_CHOICES)
    return render(request, 'auctions/create-listing.html', {
        'categories': categories
    })


@login_required(login_url='login')
def add_to_watchlist(request, item_id):
    itm = Item.objects.get(id=item_id)
    user = request.user
    try:
        wlitem = Watchlist_Item.objects.get(item=itm, user=user)
        wlitem.delete()
    except:
        wlitem = Watchlist_Item(item=itm, user=user)
        wlitem.save()

    return HttpResponseRedirect(f'/item/{item_id}')


@login_required(login_url='login')
def watchlist(request):
    user = request.user
    watchlist_items = Watchlist_Item.objects.filter(user=user)
    items = []
    for i in watchlist_items:
        items.append(i.item)

    return render(request, 'auctions/watchlist.html', {
        'items': items
    })


def categories(request):
    items = []
    chosen_cat = ''

    if request.method == 'POST':
        items = Item.objects.filter(
            category=request.POST['category'], is_sold=False)
        chosen_cat = category_choices[request.POST['category']]

    return render(request, 'auctions/categories.html', {
        'categories': Item.CATEGORY_CHOICES,
        'items': items,
        'chosen_cat': chosen_cat
    })
