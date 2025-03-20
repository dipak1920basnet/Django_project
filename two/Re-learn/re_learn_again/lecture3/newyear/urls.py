from django.urls import path, include
from . import views
urlpatterns = [
    path("",views.index, name = "new_index"),
    # path("add", views.add, name="add")
]