from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length=35)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    SectionId = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='article')
    title = models.CharField(max_length=35)
    picture = models.ImageField(blank=True)
    text = models.TextField()
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title