from django import forms
from django.forms import ModelForm
from .models import Info
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CreateForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['title', 'content', 'available', 'file', ]

        widgets = {
            'title' : forms.TextInput(
                attrs = {'class' : 'form-cotrol', 'style':'width: 100%', 
                            'placeholder': '제목을 입력하세요.', 'maxlength': '100'},
            ),
            'availabel' : forms.Select(
                attrs={'class':'custom-select'},
            ),
            'content' : forms.CharField(widget=CKEditorUploadingWidget()),
        }
    
