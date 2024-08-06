from django.db import models

from markdownx.models import MarkdownxField

# Create your models here.

    
class Profile(models.Model):
    name = models.CharField(max_length=32)
    desc = MarkdownxField()

class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=32)
    date = models.DateField()
    last_modifies = models.DateField(auto_now=True) 
    thumbnail = models.ImageField(null=True)
    content = MarkdownxField()
    