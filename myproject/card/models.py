from django.db import models

class Payment(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=12)
    end_date = models.DateTimeField()
    cvc = models.CharField(max_length=7)
    checkbox = models.BooleanField(default=False)