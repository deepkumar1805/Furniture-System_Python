from django.db import models
import datetime
from django.utils import timezone
from django import forms


# Create your models here.
class CheckOut(models.Model):
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    checkout_email = models.EmailField()
    address = models.TextField()
    product_qty = models.FloatField()
    products_id = models.CharField(max_length=50)
    username = models.CharField(max_length=30)
    Payment_status = models.CharField(max_length=10,choices=(
        ('Paid','Paid'),
        ('Pending','Pending')
    ))
    Payment_type=models.CharField(max_length=20,choices=(
        ('COD','COD'),
        ('Online','Online')
    ))
    OrderPrice=models.CharField(max_length=20)
    checkout_date =models.DateField('expiration time (of ad)', default=timezone.now() + datetime.timedelta(days=0))


    def __str__(self):
        return self.first_name