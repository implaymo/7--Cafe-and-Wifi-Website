from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cafe 

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
    
class AddCafe(forms.ModelForm):
    name = forms.CharField()
    map_url = forms.CharField()
    img_url = forms.CharField()
    location = forms.CharField()
    seats = forms.CharField()
    has_toilet = forms.BooleanField()
    has_wifi = forms.BooleanField()
    has_sockets = forms.BooleanField()
    can_take_calls = forms.BooleanField()
    coffee_price = forms.CharField()
    
    class Meta:
        model = Cafe
        fields = '__all__'
    
class EditCafe(forms.ModelForm):
    name = forms.CharField()
    map_url = forms.CharField()
    img_url = forms.CharField()
    location = forms.CharField()
    seats = forms.CharField()
    has_toilet = forms.BooleanField(required=False)
    has_wifi = forms.BooleanField(required=False)
    has_sockets = forms.BooleanField(required=False)
    can_take_calls = forms.BooleanField(required=False)
    coffee_price = forms.CharField()
    
    class Meta:
        model = Cafe
        fields = '__all__'
    