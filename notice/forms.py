from django import forms
from django.forms import ModelForm
from .models import Info
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CreateForm(forms.ModelForm):
    file = forms.FileField(required=False)
    class Meta:
        model = Info
        fields = ['title', 'content', 'available', 'file', ]

        widgets = {
            'title' : forms.TextInput(
                attrs = {'title':'제목', 'class' : 'form-cotrol', 'style':'width:80%; min-width:300px;',
                            'placeholder': '제목을 입력하세요.', 'maxlength': '100'},
            ),
            'availabel' : forms.Select(
                attrs={'title':'공개여부','class':'custom-select', 'style':'width:80%; min-width:300px;'},
            ),
            'content' : forms.CharField(widget=CKEditorUploadingWidget()),
            
        }
    
