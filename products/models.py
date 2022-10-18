from email.policy import default
from time import timezone
from django.db import models

# Create your models here.
class Foodsales(models.Model):
    Product_id = models.AutoField(primary_key = True)
    Product = models.CharField(max_length = 20)
    Category = models.CharField(max_length = 20)
    City = models.CharField(max_length = 20)
    Region = models.CharField(max_length = 20)
    Quantity = models.IntegerField()
    UnitPrice = models.FloatField()
    OrderDate = models.DateTimeField(default = timezone)


