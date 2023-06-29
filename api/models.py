from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name=models.CharField(max_length=200)


    # AbstractUser automatically sets the username,email and password

    


class Project(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    date_created=models.DateTimeField(auto_now_add=True)


class Todos(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE,default=1)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField()

