
from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index),
    path('/contact', views.contact),
    path('/about-us', views.about_us),
    path('/privacy-policy', views.privacy_policy),
]
