from django.db import models
from user.models import User
# Create your models here.
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    province = models.CharField(max_length=100,null=True)
    district = models.CharField(max_length=100,null=True)
    commune = models.CharField(max_length=100,null=True)
    detail = models.CharField(max_length=100,null=True)
