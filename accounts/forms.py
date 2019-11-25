from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django import forms
from django.forms import ModelForm
from .models import User

class CreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'age', 'gender',]
    
