from django.db import models
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    quantity=models.IntegerField()
    image=models.FileField(upload_to='uploads/',null=True)
# Create your models here.
