from django.contrib import admin
from django.urls import path
from . import views

app_name = "task"
urlpatterns = [
    path("", views.index, name="index"),
    path("add",views.add, name="add")
]