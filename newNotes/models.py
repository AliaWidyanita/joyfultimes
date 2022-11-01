from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    sender = models.CharField(max_length=255, default='')
    title = models.CharField(max_length=255,default='')
    notes = models.TextField(default='')
    date = models.DateTimeField(default=timezone.now)