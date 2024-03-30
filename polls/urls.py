from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('get_cafe_info/', views.get_cafe_info, name='get_cafe_info'),
]