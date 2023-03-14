from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index_tasks"),
    path("add", views.add, name="add_tasks")
]
