from django.db import models
from django.db.models import Index
from django.shortcuts import render

from category.models import Category


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
    vendor = models.CharField(max_length=200, blank=True)
    collections = models.CharField(max_length=200, blank=True)
    tags = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    noOfViews= models.IntegerField(default=0)
    noOfSolds = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    class Meta:
        ordering = ('name',)
        indexes = [
            Index(fields=['id', 'slug']),
        ]


    def __str__(self):
        return self.name

