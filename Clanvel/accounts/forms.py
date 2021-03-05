from django.contrib.auth import get_user_model 
from django import forms 

User = get_user_model() 

class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField()
    last_name = forms.CharField()
    password1 = forms.CharField(
        label='Paswword',
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "id": "user-password"
                   }
        )
    )  
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "id": "user-confirm-password"
                   }
        )
    )

    def clean_username(self):
        username= self.cleaned_data.get("username")
        qs = User.object.sfilter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("This is an invalid username, please pick another.")
        return username

    def clean_email(self):
        email= self.cleaned_data.get("email")
        qs = User.object.sfilter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This is an invalid email, please pick another.")
        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "id": "user-password"
                   }
        )
    )
    # def clean(self):
    #     username= self.cleaned_data.get("username")
    #     password = self.cleaned_data.get("password")
    
    def clean_username(self):
        username= self.cleaned_data.get("username")
        qs = User.object.sfilter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("This is an invalid user.")
        return username

     
