from django.urls import path, include
from django.contrib import admin 
from . import views

urlpatterns = [
    path('guest/register/', views.guest_register_view, name='guest_register'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
]