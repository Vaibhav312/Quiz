from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.



class ContactUsInfo(models.Model):
    name=models.CharField(max_length=50,error_messages={'required': 'Please enter your name'})
    email=models.EmailField(error_messages={'required': 'Please enter valid email'})
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Result(models.Model):
    total_score=models.CharField(max_length=20)
    def __str__(self):
        return self.total_score
