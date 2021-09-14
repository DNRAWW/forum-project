from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.auth.models import Group

# Register your models here.

admin.site.register(SectionGroup)

admin.site.register(Section)

class ArticleAdminForm(forms.ModelForm):
    text = forms.CharField(label='Text', widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Article
        fields = '__all__'


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm


admin.site.register(Article, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("article_Id", "user_Id")


admin.site.register(Comment, CommentAdmin)