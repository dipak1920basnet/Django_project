from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, Category, Auction_listing, Comment, Bid
from django.contrib import messages


def index(request):
    return render(request, "auctions/index.html",
                      {
                          "active_list":Auction_listing.objects.all(),
                          "Category":Category.objects.all(),
                      })
    # return render(request, "auctions/index.html")


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


## Creating a listing
@login_required
def create(request):
    return render(request, "auctions/create.html", {
        "Category":Category.objects.all(),
    })

## Get created listing data
@login_required
def create_listing(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        url = request.POST.get("url")
        category = request.POST.get("Category")
        starting_bid = int(request.POST.get("min_bid"))

        # Create category and save category if category not in category
        category_instance = Category.objects.get(category_field=category)
        owner_instance = User.objects.get(username=request.user)
        #
        # if not category_instance:
            # Category.objects.create(category_field = category)
        # category_instance = Category.objects.filter(category_field = category).first()
        #Get the name of user 
        # user = User().objects.all()
        listing = Auction_listing.objects.create(title = title, description = description,starting_bid = starting_bid, image_url=url, category=category_instance, owner=owner_instance)
        # if listing.is_valid():
        listing.save()
        
        return HttpResponseRedirect(reverse('index'))
    

## View list of categories 
def categories(request):
    return render(request, "auctions/categories.html",
                  {
                      "Category_List": Category.objects.all()
                  })

## View item from categories:
def view_item_categories(request, category_name):
    category = Category.objects.get(category_field = category_name)
    return render(request, "auctions/category_item.html",
                  {
                      "category_name":category_name,
                      "category_name_list": category.category.all()
                  })

## Add comments 
@login_required
def make_comment(request):
    if request.method == "POST":
        auction_id = request.POST.get("auction_list_id")
        auction_instance = Auction_listing.objects.get(pk=auction_id)
        comment = request.POST.get("comment")
        comments = Comment.objects.create(auction_listing=auction_instance,comment=comment)
        comments.save()

    return HttpResponseRedirect(reverse("item_detail", args=[auction_id]))


## Create watchlist:
@login_required
def watch_list(request):
    if request.method == "POST":
        list_id = request.POST.get("watch_list_id")
        auction_instance = Auction_listing.objects.get(pk=list_id)
        user_instance = request.user

        in_watchlist = auction_instance.watchlist
        if in_watchlist.filter(id=user_instance.id).exists():
            in_watchlist.remove(user_instance)
        # a1 = Watchlist(watchlist_username=user_instance)
        # a1.save()
        # a1.watchlist_listing.add(auction_instance)
        # watchlist, created = Watchlist.objects.get_or_create(watchlist_username=user_instance)

        # watchlist = Watchlist.objects.create(watchlist_username = user_instance, watchlist_listing = auction_instance)
        # watchlist.watchlist_listing.add(auction_instance)
        else:
            in_watchlist.add(user_instance)
            # in_watchlist.save()
        return HttpResponseRedirect(reverse("watchlist"))
    return HttpResponseRedirect(reverse("index"))

## View Watchlist:
@login_required
def view_watch_list(request):
        logged_in_user = request.user
        # watch_list = Auction_listing.objects.get(owner=logged_in_user)
        return render(request, "auctions/watchlist.html",
                  {
                      "active_list":Auction_listing.objects.filter(watchlist=logged_in_user),
                  })

@login_required
def bid(request):
    if request.method == "POST":
        auction_id = request.POST.get("auction_list_id")
        auction_instance = Auction_listing.objects.get(pk=auction_id)
        bidder_name = request.user
        bid = request.POST.get("current_bid")
        if bidder_name == auction_instance.owner:
            messages.error(request, "Creator cannot bid in their own auction list")
        else:
            
            current_bidding_amount = Bid.objects.filter(auction_listing = auction_instance).last()

            
            if current_bidding_amount == None:
                    ## Create a bid
                bids = Bid.objects.create(auction_listing=auction_instance,bidder_name=bidder_name,bidding_amount=bid)
                bids.save()
            elif int(bid) <= int(auction_instance.starting_bid) or current_bidding_amount.bidding_amount >= int(bid):
                messages.error(request, f""" Your bid is {bid}
                            Place bid higher than the leading bid or starting bid""")
            else:
                    ## Update a bid 
                current_bidding_amount.bidding_amount = bid
                current_bidding_amount.save()
                messages.success(request,"Bid placed successfully")
            return HttpResponseRedirect(reverse("item_detail", args=[auction_id]))
        return HttpResponseRedirect(reverse("item_detail", args=[auction_id]))
    return HttpResponseRedirect(reverse("index"))


##View Item details:
 
def view_item_details(request, number):
    # watch = request.session.get('watch','Add to WatchList')
    item_number = Auction_listing.objects.get(pk=number)
    # bidder_name = User.objects.get(pk=number)
    # bidding_number = Bid.objects.get(pk=number)
    bids = Bid.objects.filter(auction_listing = item_number).last()
    
    if bids == None:
        bids = item_number.starting_bid
    ### Declare winner
    ## Get the bidder name 
    message = None
    find = False
    if item_number.is_active == False:
        bidder = Bid.objects.filter(auction_listing = item_number).last()
        bidder_name = bidder.bidder_name
        if bidder_name == request.user:
            find = True
            message = "You have won this auction"

    if item_number.owner == request.user:
        close = True
    else:
        close = False
    return render(request, "auctions/item_detail.html",
                  {
                      "item_detail": item_number,
                      "Comments":item_number.auction_llist.all(),
                    #   "bidder_name":item_number.list.bidder,
                      "bids":bids,
                      "messaging":message,
                    "watching":"Toogle Watch List",
                    "close":close,
                    "find":find
                  })

#### Close Listing and declare winner
## Ckise listing:
def close_listing(request):
    if request.method == "POST":
        auction_id = request.POST.get('close_item')
        auction_instance = Auction_listing.objects.get(pk=auction_id)
        ## Check if bidding has started or not 
        bids = Bid.objects.filter(auction_listing = auction_id).last()
        if bids == None:
            messages.error(request,"Cannot close as starting bid is equal to leading")
            return HttpResponseRedirect(reverse("item_detail", args=[auction_id]))
        auction_instance.is_active = False
        auction_instance.save()
        messages.success(request,"Listing has been closed")
        return HttpResponseRedirect(reverse("item_detail", args=[auction_id]))
        
        
## View Closed item list:
def closed_item_list(request):

    return render(request, "auctions/closed_listing.html",
                      {
                          "active_list":Auction_listing.objects.all(),
                          "Category":Category.objects.all(),
                      })