from django.db import models
from django.db.models import Index


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    stock_quantity = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=200, db_index=True)


    class Meta:
        ordering = ('name',)
        indexes = [
            Index(fields=['id', 'slug']),
        ]


    def __str__(self):
        return self.name

