from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("chat/", views.chat_list, name="chat_list"), 
    path("send/", views.send_message, name="send_message"),
    path("register/", views.register, name="register"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("login/", views.login, name="login")
    ]