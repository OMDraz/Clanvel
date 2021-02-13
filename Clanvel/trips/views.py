from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm

def index(request):
    context = {}
    return render(request, 'base.html', context)

def signup(request):
    if request.method == 'POST':
        f = SignUpForm(request.POST, instance = request.user)
        if f.is_valid():
            f.save()
    else:
        f = SignUpForm(request.POST , instance = request.user)

    print "UserDetails objects: ", (UserProfile.objects.all()) 
    return render(request, 'signup.html', {'form': form})

def logout_request(request):
    logout(request)
    messages.info(request, 'Logged out successfully!')
    return redirect("index")