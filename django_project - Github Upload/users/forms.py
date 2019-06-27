# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    
    class Meta:
        model = User
        fields = ['username',"first_name", "last_name", "email"]
        
            
            
class UserUpdateForm(forms.ModelForm):
    first = forms.TextInput()
    last = forms.TextInput()
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
class ProfileUpdateForm(forms.ModelForm):
    bio = forms.Textarea()
    class Meta:
        model = Profile
        fields = ['image', 'bio']