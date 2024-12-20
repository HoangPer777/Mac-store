from django.db import models

from coupon.models import Coupon
from user.models import User


class Order(models.Model):
    createAt = models.DateTimeField(auto_now_add=True)
    paymentStatus =models.CharField(max_length=50)
    dateOrder = models.DateField(auto_now=True)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    couponID = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=50)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)