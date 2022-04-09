from distutils.command.upload import upload
from itertools import product
from turtle import title
from unicodedata import category
from django.db import models

# Create your models here.

  

class Product(models.Model):
    title = models.CharField(max_length=30)
    pid = models.CharField(primary_key = True,max_length=30)
    desp = models.TextField()
    img = models.ImageField(upload_to='image')
    price = models.IntegerField()
    quantity = models.IntegerField()
    weight = models.IntegerField()
    weightunit = models.CharField(max_length=12)
    category = models.CharField(max_length=12)
    subcategory = models.CharField(max_length=12)
    vendor = models.CharField(max_length=12)
    
    def __str__(self):
        return self.title

class Orders(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quan=models.IntegerField()
    # price= models.CharField(max_length=30)

class Details(models.Model):
    name=  models.CharField(max_length=30)  
    phone =models.CharField(max_length=10)  
    email=  models.CharField(max_length=30)  
    password=  models.CharField(max_length=30)  

