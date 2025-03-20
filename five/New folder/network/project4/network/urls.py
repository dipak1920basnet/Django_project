
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("make_post",views.make_post, name="make_post"),
    path("profile/<int:id>",views.profile, name="profile"),
    path("following>", views.following, name="following"),
    path("follow/<int:id>",views.follow,name="follow"),
    path("like/<int:id>", views.like, name="like")
]
