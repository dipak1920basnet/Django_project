from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.home, name = "home"),
    path("api/tasks",views.get_tasks , name="get_tasks"),
    path("api/add_task",views.add_task , name="add_task"),
    path("api/delete_task/<int:task_id>",views.delete_task , name="delete_task"),
]
