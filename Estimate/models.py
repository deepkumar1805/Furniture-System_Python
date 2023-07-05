from django.db import models

# Create your models here.

class Estimate(models.Model):
    apartment_type = models.CharField(max_length=10,choices=(
        ('2bhk',"2bhk"),
        ('3bhk',"3bhK"),
        ('3.5bhk',"3.5bhk"),
        ('4bhk',"4bhk")
    ))

    bedroomes_type = models.CharField(max_length=50,choices=(
        ('Master Room','Master Room'),
        ('Home Office Study',"Home Office Study"),
        ('Parents',"Parents"),
        ('Kids Bedroom',"Kids Bedroom"),
        ('Kids Room 1',"Kids Room 1"),
        ('Kids Room 2',"Kids Room 2"),
        ('Guest Bedroom',"Guest Bedroom")
    ))

    modular_kitchen = models.CharField(max_length=3,choices=(
        ('Yes',"Yes"),
        ('No',"No")
    ))

    Carpet_area_in_sqft = models.CharField(max_length=10)