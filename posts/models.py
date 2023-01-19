from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    descriptions = models.TextField()
    created_date = models.DateField(auto_now=True)
