from django import forms
from django.forms import ModelForm
from .models import Info

class CreateForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['title', 'content',]
    
