from importlib.metadata import requires

from django.utils.timezone import now


from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# chỉ giảm theo phần trăm, có hạn mức giá trị lớn nhất,
class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True) # mã
    type = models.CharField(max_length=20)
    percent = models.IntegerField(null=True, blank=True,validators=[MinValueValidator(0), MaxValueValidator(100)]) # %giảm
    amount = models.IntegerField(null=True, blank=True)
    maxValue = models.DecimalField(max_digits=10, decimal_places=2) # nếu theo % thì giảm max bao nhiêu
    forProduct = models.IntegerField(null=True, blank=True)

    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    active = models.BooleanField(default=True, blank=True)
    remaining = models.PositiveIntegerField() # còn lại

    def __str__(self):
        return self.code

