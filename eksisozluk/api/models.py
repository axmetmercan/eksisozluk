from email.policy import default
from pyexpat import model
from random import choices
from tkinter import CASCADE
from xml.etree.ElementTree import TreeBuilder
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

USER_TYPES = [

        ('BG', 'Beginner'),
        ('MD', 'Middle'),
        ('PR', 'Proffessional')
]

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)



class User(AbstractUser):
    # username = models.CharField(max_length=20, verbose_name='User Name')
    # name = models.CharField(max_length=20, verbose_name= 'Name')
    # surname = models.CharField(max_length=20, verbose_name= 'Surname')
    # email = models.EmailField(verbose_name="Email")   
    total_likes = models.IntegerField(verbose_name="User Status", default=0)
    status = models.CharField(max_length=2, choices = USER_TYPES, default = 'BG')

    def __str__(self):
        return self.username





class Tag(models.Model):
    name = models.CharField(verbose_name="Tag Name", max_length=20)
    
    def __str__(self):
        return self.name



    
class Title(models.Model):
    name = models.CharField(verbose_name='Title', max_length=65)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Created By', blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='tag')
    total_click = models.PositiveIntegerField(default=0, null= True, blank=True)

    def __str__(self):
        return self.name


class Explanation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name = "title")
    content = models.CharField(verbose_name='Post Copntent', max_length=255)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    status = models.BooleanField(default = True)
    like = models.IntegerField(verbose_name="Like Count", default=0)

    def __str__(self):
        return self.content



class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80, verbose_name='Blog Title', blank=False, null = False, default="")
    content = models.TextField(verbose_name='Blog Content Text')
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)

    status = models.BooleanField(default=True)
    like = models.IntegerField(verbose_name='Total Likes of Blog Post')
    created_date = models.DateTimeField(verbose_name='Created Ddate', auto_now_add=True)

    def __str__(self):
        return self.title