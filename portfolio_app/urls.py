from django.urls import path
from . import views

urlpatterns = [
    path('', views.static_home, name='home-page'),
    path('home', views.home, name='home-page'),
    path('about', views.about, name='about-me'),
    path('projects/<str:pk>', views.projects, name='projects'),
]