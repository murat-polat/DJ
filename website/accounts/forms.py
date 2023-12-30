from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput, EmailInput, PasswordInput
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']
        widgets = {
            "username": TextInput(attrs={
                
            "placeholder": "username"
        }),
            "email": EmailInput(attrs={
                
            "placeholder": "email"
        }),
            "password1": PasswordInput(attrs={
                
            "placeholder": "password"
        }),

            "password2": PasswordInput(attrs={
                
            "placeholder": "Confirm password"
        }),
        
        }

        error_messages = {
            'username': {
                'unique': 'This username is already taken. Please choose a different one.',
            },
            'password2': {
                'password_mismatch': 'The two password fields do not match.',
            },
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    # email = forms.CharField(widget=EmailInput())
    password = forms.CharField(widget=PasswordInput())