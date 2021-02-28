from django.contrib.auth import authenticate, login, get_user_model, logout
from django.urls import reverse_lazy 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, FormView
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url
from django.contrib import messages 
from django.contrib.auth.views import LoginView


from .forms import LoginForm, RegisterForm


class SignUpView(FormView):
    template_name = 'registration/login.html'
    form_class = RegisterForm 
    success_url = reverse_lazy("home")

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/success/')
        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
            user.verify_email()
        return super().form_valid(form)

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



