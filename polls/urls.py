from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cafe", views.get_all_cafes, name="get_all_cafes")
]