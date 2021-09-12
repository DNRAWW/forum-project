from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class SectionGroup(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name

class Section(models.Model):
    groupId = models.ForeignKey(SectionGroup, on_delete=models.CASCADE, related_name='sections')
    name = models.CharField(max_length=35)
    tags = TaggableManager(blank=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    SectionId = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=35)
    picture = models.ImageField(blank=True)
    text = models.TextField()
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title