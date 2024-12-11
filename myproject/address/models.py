from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Address(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    province = models.CharField(max_length=100,null=True)
    district = models.CharField(max_length=100,null=True)
    commune = models.CharField(max_length=100,null=True)
    detail = models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=11,null=True)
    type = models.CharField(max_length=50,null=True)
