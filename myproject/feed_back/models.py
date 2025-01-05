from django.db import models
from customer.models import Customer
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import now


class Feedback(models.Model):
    customerID = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank = True)
    rating = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    type = models.IntegerField(choices=[(1, 'Toxic'), (0, 'Not Toxic')], null=True, blank=True)  # None = chưa phân loại
