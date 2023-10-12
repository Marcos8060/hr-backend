from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    permissions = models.ManyToManyField(Permission, blank=True)

    def __str__(self):
        return self.name
    

class Employee(AbstractUser):
    # Add any additional fields specific to employees
    full_name=models.CharField(max_length=30)
    email=models.EmailField()
    occupation=models.CharField(max_length=200)
    role=models.ForeignKey(Role,on_delete=models.CASCADE,null=True,blank=True)


class Leave(models.Model):
    leave_type=models.CharField(max_length=200)
    date_from=models.DateTimeField(auto_now_add=False)
    date_to=models.DateTimeField(auto_now_add=False)
    number_of_days=models.IntegerField()
    reason=models.CharField(max_length=400)

    def __str__(self):
      return self.leave_type


class Permission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

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


