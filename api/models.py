from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=240,unique=True)
    password=models.CharField(max_length=200)
    username=models.CharField(max_length=200)

    # set email as default
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Project(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    date_created=models.DateTimeField(auto_now_add=True)


class Todos(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE,default=1)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField()

