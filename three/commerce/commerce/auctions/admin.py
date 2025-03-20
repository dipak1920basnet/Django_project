from django.contrib import admin

# Register your models here.

from .models import User, AuctionList, Bids, Comment

admin.site.register(User)
admin.site.register(AuctionList)
admin.site.register(Bids)
admin.site.register(Comment)

