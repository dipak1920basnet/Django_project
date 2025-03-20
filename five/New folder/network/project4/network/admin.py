from django.contrib import admin

# Register your models here.
from .models import User, Create_posting, Like, Followers, Comment

admin.site.register(User)
admin.site.register(Create_posting)
admin.site.register(Like)
admin.site.register(Followers)
admin.site.register(Comment)