from django.contrib.auth import authenticate, login, get_user_model, logout
from django.urls import reverse_lazy 
from django.views.generic import CreateView, FormView
from django.shortcuts import redirect
from django.contrib import messages 

from .forms import LoginForm, RegisterForm


class SignUpView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/login/'

class LoginView(FormView):
    """
    Validates the Login of the account
    """
    template_name = 'registration/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

def LogoutView(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('/')



