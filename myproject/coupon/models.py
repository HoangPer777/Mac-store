from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# chỉ giảm theo phần trăm, có hạn mức giá trị lớn nhất, type(????): cho product và customer
class Coupon(models.Model):
    code = models.CharField(max_length=10, unique=True) # mã
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)]) # %giảm
    maxValue = models.DecimalField(max_digits=10, decimal_places=2) # nếu theo % thì giảm max bao nhiêu
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    active = models.BooleanField()
    remaining = models.PositiveIntegerField() # còn lại
    type = models.CharField(max_length=10) # cho product or customer
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0) # giảm theo số tiền
    sku = models.CharField(max_length=10, default='default-sku') # mã sản phẩm

    def __str__(self):
        return self.code

