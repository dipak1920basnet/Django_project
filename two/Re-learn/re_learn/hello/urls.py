from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("brian/", views.brian, name="brian"),
    path("main/<str:name>",views.main_one,name="main_one"),
    path("<str:name>", views.greet, name="greet"),
    path("world/<str:name>", views.temp, name="greet"),
]
