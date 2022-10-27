from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255)
    body = models.TextField()
