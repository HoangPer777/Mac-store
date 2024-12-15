from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(User,null=True,blank=True,max_length=100)
    name = models.CharField(null=True,blank=True,max_length=100)
    email = models.CharField(null=True,blank=True,max_length=100)
    def __str__(self):
        return self.username