from django import forms
from .models import UserProfile, Blog

class Loginform(forms.Form):
    username = forms.CharField(label="Enter username",error_messages = {'required': ""})
    password = forms.CharField(label="Enter password", max_length=50, widget=forms.PasswordInput,error_messages = {'required': ""})

class Registerform(forms.Form):
    username = forms.CharField(label="Enter username",error_messages = {'required': ""})
    password = forms.CharField(label="Enter password", max_length=50, widget=forms.PasswordInput,error_messages = {'required': ""})
    email=forms.EmailField(label="email id :",error_messages = {'required': ""})



