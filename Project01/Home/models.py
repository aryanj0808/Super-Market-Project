from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()


    def __str__(self):
        return self.name

class Product(models.Model):
    product_name=models.CharField(max_length=30)
    price=models.CharField(max_length=50)
    discount=models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()


    def __str__(self):
        return self.product_name