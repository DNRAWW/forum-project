from django.shortcuts import redirect, render
from main.models import *
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

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


def register(request):
    form = UserCreationForm

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect(login)

    return render(request, 'register.html', {'title':'Sign up', 'form':form})

def login(request):
    form = UserCreationForm
    return render(request, 'login.html', {'title':'Login', 'form':form})