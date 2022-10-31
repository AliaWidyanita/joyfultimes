from email.policy import default
from statistics import mode
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Notes(models.Model):
    sender = models.CharField(max_length=255, default='')
    title = models.CharField(max_length=255,default='')
    notes = models.TextField(default='')
    
