from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("",views.index, name="index"),
    path("sections/<int:num>", views.section, name="section"),
    path("scroll", views.scroll, name="scroll"),
    # path("post",views.posts, name="posts"),

]
