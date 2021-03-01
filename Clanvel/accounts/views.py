from django.contrib.auth import authenticate, login, get_user_model, logout
from django.urls import reverse_lazy 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, FormView
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url
from django.contrib import messages 
from django.contrib.auth.views import LoginView

from .models import User 
from .forms import LoginForm, RegisterForm


class SignUpView(CreateView):
    model = User 

    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.post_date = datetime.now()
        instance.save()
        return redirect(self.get_success_url())
    def get(self, request, *args, **kwargs):
        context = {'form': RegisterForm()}
        return render(request, 'registration/register.html', context)

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            User = form.save()
            User.save()
            return HttpResponseRedirect(reverse_lazy('home'))
        return render(request, 'registration/register.html', {'form': form})

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



