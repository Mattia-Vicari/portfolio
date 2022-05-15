from django.shortcuts import render
from django.http import HttpResponse
import os
def static_home(response):
    return render(response, 'portfolio_app/home.html', {})

def home(response):
    return render(response, 'portfolio_app/home.html', {})

def about(response):
    return render(response, 'portfolio_app/about.html', {})

def projects(response, pk):
    return render(response, 'portfolio_app/projects.html', {"title": pk})