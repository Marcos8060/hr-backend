from django.db import models
from django.contrib.auth.models import AbstractUser,Permission

# Create your models here.

class User(AbstractUser):
    name=models.CharField(max_length=200)



class Permission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name



class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    permissions = models.ManyToManyField(Permission, blank=True)

    def __str__(self):
        return self.name
    

STATUS_CHOICES=(
    ('in progress','IN PROGRESS'),
    ('completed','COMPLETED'),
    ('under review','UNDER REVIEW'),
    ('on hold','ON HOLD'),
)

class Project(models.Model):
    name=models.CharField(max_length=200)
    status=models.CharField(max_length=30,choices=STATUS_CHOICES,default='in progress')
    date_created=models.DateTimeField(auto_now_add=True)


class ApprovedProject(models.Model):
    name=models.CharField(max_length=200)
    status=models.CharField(max_length=30,choices=STATUS_CHOICES,default='in progress')
    date_created=models.DateTimeField(auto_now_add=True)


