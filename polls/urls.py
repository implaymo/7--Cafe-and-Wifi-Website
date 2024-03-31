from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('get_cafe_info/', views.get_cafe_info, name='get_cafe_info'),
    path("login/", views.login, name="login"),
    path("sign_up/", views.sign_up, name="sign_up")
    
]