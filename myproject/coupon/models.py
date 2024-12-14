from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# chỉ giảm theo phần trăm, có hạn mức giá trị lớn nhất,
class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True) # mã
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)]) # %giảm
    maxValue = models.DecimalField(max_digits=10, decimal_places=2) # nếu theo % thì giảm max bao nhiêu
    from_date = models.DateTimeField() 
    to_date = models.DateTimeField()
    active = models.BooleanField(default=True) 
    remaining = models.PositiveIntegerField() # còn lại
    sku = models.CharField(max_length=10, default='all') # mã sản phẩm

    def __str__(self):
        return self.code

