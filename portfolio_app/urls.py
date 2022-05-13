from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi, name='home-page'),
    path('home', views.home, name='home-page'),
    path('about', views.about, name='about-me'),
]