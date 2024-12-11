from django.db import models
from django.db.models import Index
from django.shortcuts import render

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    image = models.CharField(max_length=200)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    stock_quantity = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=200, db_index=True)
    vendor = models.CharField(max_length=200, blank=True)  # Thêm trường nhà cung cấp
    collections = models.CharField(max_length=200, blank=True)  # Thêm trường bộ sưu tập
    tags = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    noOfViews= models.IntegerField(default=0)
    noOfSolds = models.IntegerField(default=0)

    class Meta:
        ordering = ('name',)
        indexes = [
            Index(fields=['id', 'slug']),
        ]


    def __str__(self):
        return self.name

