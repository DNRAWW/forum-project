from django import forms
from django.forms import widgets
from .models import *
from ckeditor.widgets import CKEditorWidget

class CommentForm(forms.ModelForm):
    text = forms.CharField(min_length=5, max_length=1000, widget=forms.Textarea(attrs={
        'rows':'5',
    }))

    class Meta:
        model = Comment
        fields = ('text', )

class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=50, 
            widget=forms.TextInput(attrs={
                'placeholder':'Title'
            }))
    text = forms.CharField(min_length=5, max_length=3000, widget=CKEditorWidget())

    class Meta:
        model = Article
        fields = ('title', 'text')