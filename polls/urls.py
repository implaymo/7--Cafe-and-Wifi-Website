from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('get_cafe_info/', views.get_cafe_info, name='get_cafe_info'),
    path("sign_in/", views.sign_in, name="sign_in"),
    path("register/", views.register, name="register")
    
]