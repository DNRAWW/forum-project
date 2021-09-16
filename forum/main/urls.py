from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('section/<int:pk>/', views.section, name='section'),
    path('article/<int:pk>/', views.article, name='article'),
    path('user/<int:pk>/', views.user, name='user'),
    path('signup', views.register, name='signup'),
    path('login', views.login, name='login')
]