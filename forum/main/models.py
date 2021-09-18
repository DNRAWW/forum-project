from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SectionGroup(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name


class Section(models.Model):
    group_Id = models.ForeignKey(SectionGroup, on_delete=models.CASCADE, related_name='sections')
    name = models.CharField(max_length=35)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    user_Id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    Section_Id = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=50)
    picture = models.ImageField(blank=True)
    text = models.TextField()
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user_Id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usr_comments')
    article_Id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    time = models.DateTimeField(auto_now=True)