from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# chỉ giảm theo phần trăm, có hạn mức giá trị lớn nhất, type(????): cho product và customer
class Coupon(models.Model):
    code = models.CharField(max_length=10, unique=True)
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    maxValue = models.DecimalField(max_digits=10, decimal_places=2)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    active = models.BooleanField()
    remaining = models.PositiveIntegerField()
    type = models.CharField(max_length=10)

    def __str__(self):
        return self.code

