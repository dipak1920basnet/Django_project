from django.contrib import admin

from .models import Category, User, Auction_listing,Comment,Bid
# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Auction_listing)
admin.site.register(Bid)
admin.site.register(Comment)
# admin.site.register(Watchlist)
