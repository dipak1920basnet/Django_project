from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:number>",views.view_item_details, name="item_detail"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create",views.create, name="create"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("categories",views.categories, name="categories"),
    path("categories/<str:category_name>", views.view_item_categories, name="view_item_categories"),
    path("comment", views.make_comment, name="make_comment"),
    path("bid",views.bid, name="bid"),
    path("watch_list", views.watch_list, name="watch_list"),
    path("watchlist", views.view_watch_list, name="watchlist"),
    path("close_listing", views.close_listing, name='close_listing'),
    path("closed_items", views.closed_item_list, name="closed_items"),
    # path("")
]
