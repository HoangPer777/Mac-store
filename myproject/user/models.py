from django.db import models


class User(models.Model):
    full_name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100)
    birth =models.DateField(null=True)
    gender =models.CharField(max_length=20)
    email =models.EmailField(null=True)
    phone =models.CharField(max_length=20)
    address =models.CharField(max_length=50)
    password =models.CharField(max_length=100)


    def __str__(self):
        return self.full_name + ' ' + self.display_name + ' ' + self.birth +' '+ self.gender + ' ' + self.email + ' ' + self.phone + ' ' + self.address