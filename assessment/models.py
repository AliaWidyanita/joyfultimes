from django.db import models
from django.contrib.auth.models import User


# Assessment model
class MentalHealthAssessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    topic = models.IntegerField(default=0)
    result = models.CharField(max_length=30)