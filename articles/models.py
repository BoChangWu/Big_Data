from operator import mod
from pyexpat import model
from django.db import models
from django.forms import IntegerField

# Create your models here.
class Article(models.Model):
    content = models.TextField(blank=True,null=True)
    img_url = models.CharField(max_length=200)
    article_id = models.IntegerField()
    article_order = models.CharField(max_length=30) # No.0為Title 跟Cover
    related_art = models.CharField(max_length=200)

class Art(models.Model):
    title = models.CharField(max_length=300)
    cover= models.TextField(blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    art_id = models.IntegerField()

class Img(models.Model):
    url = models.TextField(blank=True,null=True)
    art_id = models.IntegerField()

class Related(models.Model):
    url = models.TextField(blank=True,null=True)
    art_id = models.IntegerField()