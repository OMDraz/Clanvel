from django.contrib.auth import authenticate, login, get_user_model, logout
from django.urls import reverse_lazy 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, FormView
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url
from django.contrib import messages 

from .forms import LoginForm, RegisterForm, GuestForm
from .models import GuestEmail


def guest_register_view(request):
    form = GuestForm(request.POST or None)
    context = {
        'form': form 
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None 
    if form.is_valid():
        email = form.cleaned_data.get('email')
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id 
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect('/register/')
    return redirect('registration/guest_register.html')

class SignUpView(request):
    if response.method == "POST":
	    form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            
        return redirect("/home")
    else:
	    form = RegisterForm()
    return render(response, "register/register.html", {"form":form})

class LoginView(FormView):
    form_class = LoginForm 
    success_url = '/'
    template_name = 'registration/login.html'

    def form_valid(self, form):
        request = self.request 
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None 
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass 
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect('/')
        return super(LoginView, self).form_invalid(form)


def LogoutView(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('/')

