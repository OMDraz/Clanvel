from django.http import HttpResponse
from django.shortcuts import render, redirect 

def index(request):
    context = {}
    return render(request, 'base.html', context)

def signup(request):
    context = {} 
    return render(request, 'signup.html', context)