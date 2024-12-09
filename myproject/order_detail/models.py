from django.db import models

# Create your models here.
class OrderDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
