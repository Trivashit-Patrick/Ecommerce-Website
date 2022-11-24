import email
from django.db import models
from datetime import datetime

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    email= models.CharField(max_length=100 ,default='')
    address = models.CharField(max_length=150)
    phoneNumber = models.CharField(max_length=15)
    city = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    timeStamp=models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.name