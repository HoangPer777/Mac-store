from django.db import models

from user.models import User


class Order(models.Model):
    createAt = models.DateTimeField(auto_now_add=True)
    paymentStatus =models.CharField(max_length=50)
    orderStatus =models.CharField(max_length=50)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)