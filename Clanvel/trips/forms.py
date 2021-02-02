from django.forms import ModelForm
from manager.models import Person


class RegisterForm(ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=PasswordInput)
    email = forms.CharField(widget=PasswordInput)
    city_name = forms.CharField(max_length=100, label='City')
    state_name = forms.CharField(max_length=100, label='State')

    class Mega:
        model = Person 
        fields = [
            "username", "password", "email", "city_name", "state_name"
        ]


