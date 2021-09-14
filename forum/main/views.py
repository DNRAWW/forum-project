from django.shortcuts import render
from main.models import *

# Create your views here.
def index(request):
    groups = SectionGroup.objects.all()
    return render(request, 'index.html', {'title': 'Home page', 'groups':groups})


def section(request, pk):
    section = Section.objects.get(id=pk)
    return render(request, 'section.html', {'title':section.name, 'section':section})


def article(request, pk):
    article = Article.objects.get(id=pk)
    return render(request, 'article.html', {'title':article.title, 'article':article})


def user(request, pk):
    user = User.objects.get(id=pk)
    return render(request, 'user.html', {'title':user.username, 'user':user})

