from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('get_cafe_info/', views.get_cafe_info, name='get_cafe_info'),
    path("sign_in/", views.sign_in, name="sign_in"),
    path("register/", views.register, name="register"),
    path("logout_view/", views.logout_view, name="logout_view"),
    path("add_new_cafe/", views.add_new_cafe, name="add_new_cafe"),
    path("edit_cafe_selected/", views.edit_cafe_selected, name="edit_cafe_selected"),
    path("delete_cafe/", views.delete_cafe, name="delete_cafe"),
    path("google_m/", views.google_m, name="google_m"),
]
