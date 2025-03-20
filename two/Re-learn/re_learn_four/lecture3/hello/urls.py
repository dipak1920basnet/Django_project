from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("<str:name>", views.greet, name="greet")
]
