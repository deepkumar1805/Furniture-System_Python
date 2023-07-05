from django.db import models

# Create your models here.
class product(models.Model):
    category_name=models.ForeignKey("category.Category",on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    price=models.FloatField()
    qty=models.FloatField()
    image=models.ImageField(upload_to="img/ProductImg/")
    description=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Reviews(models.Model):
    product_review=models.ForeignKey(product,on_delete=models.CASCADE,null=True,default=1)
    reviews=models.TextField()
    name=models.CharField(max_length=20)
    email=models.EmailField()


    def __str__(self):
        return self.name