from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email_address = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    first_name = forms.CharField(max_length=30, required=True, help_text='What is your name?')
    last_name = forms.CharField(max_length=30, required=True, help_text='What is your last name?')
    location = forms.CharField(max_length=30, required=True, help_text='What is your location?')
    interested_in_friends = forms.BooleanField()
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2020)))