from django.db import models

# Create your models here.
class Contactus(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    msg=models.TextField()


    def __str__(self):
        return self.name
    
    