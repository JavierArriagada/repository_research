from django import forms
from .models import Page

class PageForm(forms.ModelForm): #modelo de formulario

    class Meta:

        model = Page
        fields = ['title', 'content', 'order'] #, 'pdf', 'cover'
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Orden'}),
            'pdf': forms.FileInput(attrs={'class':'form-control-file mt-3'}),
            #'cover': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
        }
        labels = {
            'title':'', 'order':'',
        }