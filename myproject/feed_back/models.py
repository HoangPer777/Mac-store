from django.db import models
from user.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import now
from product.models import Product


class Feedback(models.Model):
    userID = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank = True)
    productID = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank = True)
    rating = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    type = models.IntegerField(choices=[(1, 'Toxic'), (0, 'Not Toxic')], null=True, blank=True)  # None = chưa phân loại
