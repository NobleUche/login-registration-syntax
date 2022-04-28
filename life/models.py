from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100,blank=False)
    password = models.CharField(max_length=100,blank=False)
    email = models.CharField(max_length=100,blank=False)


  