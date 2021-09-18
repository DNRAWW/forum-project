from django.shortcuts import redirect, render
from main.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    groups = SectionGroup.objects.all()
    return render(request, 'index.html', {'title': 'Home page', 'groups':groups})


def section(request, pk):
    section = Section.objects.get(id=pk)
    articles = section.articles.all()
    paginator = Paginator(articles, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'section.html', {'title':section.name, 'section':section, 'articles':page_obj})

@login_required(login_url='/login')
def article(request, pk):
    article = Article.objects.get(id=pk)

    paginator = Paginator(article.comments.all(), 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    new_comment = None
    form = CommentForm

    if request.method == 'POST':
        user_Id = request.user
        article_Id = Article.objects.get(id=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user_Id = user_Id
            new_comment.article_Id = article_Id
            new_comment.save()
            url = reverse_lazy('article', kwargs={'pk': article_Id.id}) + '?page=' + page_number
            return redirect(url)

    
    return render(request, 'article.html', {'title':article.title, 'article':article, 'form':form, 'comments':page_obj})


def user(request, pk):
    user = User.objects.get(id=pk)
    articles = user.articles.all()

    paginator = Paginator(articles, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'user.html', {'title':user.username, 'user':user, 'articles':page_obj})


def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='User')
            user.groups.add(group)
            return redirect('login')
        
        else:
            print(form.errors)

    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'title':'Sign up', 'form':form})


def loginUser(request):
    form = AuthenticationForm

    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or password is incorrect')
            return render(request, 'login.html', {'title':'Login', 'form':form})
    
    return render(request, 'login.html', {'title':'Login', 'form':form})


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login')
def new_article(request, pk):
    section = Section.objects.get(id=pk)
    form = ArticleForm
    new_article = None

    if request.method == 'POST':
        user_Id = request.user
        form = ArticleForm(request.POST)
        section_Id = section
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.user_Id = user_Id
            new_article.Section_Id = section_Id
            new_article.save()
            return redirect('section', pk)
    return render(request, 'new_article.html', {'title':'New article ' + section.name, 'section':section, 'form':form})
