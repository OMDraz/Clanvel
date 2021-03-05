from django.contrib.auth import authenticate, login, logout 
from django.shortcuts import render, redirect  

#Create your views here 
from .forms import LoginForm, RegisterForm

#Finished part 1: https://www.youtube.com/watch?v=x8yxM7rCvEc


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        try: 
            user = User.objects.create_user(username, email, password)
        except:
            user = None
        if user != None:
            login(request, user) 
            return redirect('/')
    return render(request, "registration/register.html", {"form": form})


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(
                request, 
                username=username, 
                password=password
            )
        if user == None:
            # attempt = request.session.get("attempt") or 0
            # request.session['attempt'] = attempt + 1 
            # return redirect('/invalid-password')
            request.session['invalid_user'] = 1 
            return render(request, "registration/register.hml",{ "form": form, "invalid_user":True})
        login(request, user) 
        return redirect('/')
    return render(request, "registration/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect('/login')
