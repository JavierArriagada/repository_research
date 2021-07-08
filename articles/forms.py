from django import forms
from .models import Article

class ArticleForm(forms.ModelForm): #modelo de formulario

    class Meta:

        model = Article
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Orden'}),
        }
        labels = {
            'title':'', 'order':'',
        }

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()