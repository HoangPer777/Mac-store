from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100, null=True)
    birth = models.DateField(null=True)
    gender =models.CharField(max_length=20, null=True)
    email =models.EmailField(null=True, unique=True)
    phone =models.CharField(max_length=20, null=True)
    password =models.CharField(max_length=100)

