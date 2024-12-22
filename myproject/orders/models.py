from django.db import models

from coupon.models import Coupon
from user.models import User


class Order(models.Model):
    paymentStatus =models.CharField(max_length=50)
    dateOrder = models.DateField(auto_now=True)
    totalPrice = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    couponID = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True,  blank = True)
    paymentMethod = models.CharField(max_length=100, default='cash')
    userId = models.ForeignKey(User, on_delete=models.CASCADE)