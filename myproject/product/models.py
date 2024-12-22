from cloudinary.models import CloudinaryField
from django.db import models
from django.db.models import Index

from category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    stock_quantity = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=200, db_index=True)
    vendor = models.CharField(max_length=200, blank=True)
    collections = models.CharField(max_length=200, blank=True)
    tags = models.CharField(max_length=200, blank=True)
    noOfViews = models.IntegerField(default=0)
    noOfSolds = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    class Meta:
        ordering = ('name',)
        indexes = [
            Index(fields=['id', 'slug']),
        ]

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image')
    is_primary = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_primary:
            # Ensure only one primary image per product
            ProductImage.objects.filter(product=self.product, is_primary=True).exclude(pk=self.pk).update(is_primary=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {'Primary' if self.is_primary else 'Secondary'}"

    def get_image_url(self):
        if self.image:
            return self.image.url
        return None