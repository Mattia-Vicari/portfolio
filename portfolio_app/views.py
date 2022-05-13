from django.shortcuts import render
from django.http import HttpResponse
import os
def hi(request):
    return HttpResponse('<h1>This is my home page</h1>')

def home(response):
    return render(response, 'portfolio_app/home.html', {})

def about(response):
    return render(response, 'portfolio_app/about.html', {})