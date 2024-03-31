from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        
class LoginForm(User):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)