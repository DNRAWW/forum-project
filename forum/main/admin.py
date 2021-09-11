from django.contrib import admin
from .models import Section
from .models import Article
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.auth.models import Group

# Register your models here.

admin.site.unregister(Group)

admin.site.register(Section)

class ArticleAdminForm(forms.ModelForm):
    text = forms.CharField(label='Text', widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Article
        fields = '__all__'


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm

admin.site.register(Article, ArticleAdmin)