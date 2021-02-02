from django.http import HttpResponse
from django.shortcuts import render, redirect 
from django import forms
from .forms import RegisterForm

def index(request):
    context = {}
    return render(request, 'base.html', context)

def signup(request):
    context = {}
    context['form'] = RegisterForm()
    return render(request, 'signup.html', context)