from django.db import models

# Create your models here.
class Urgence(models.Model):
    lantitude= models.DecimalField(max_length=10,max_digits=5, decimal_places=2)
    longitude=models.DecimalField(max_length=10,max_digits=5, decimal_places=2)
    descreption=models.TextField(max_length=10, null=True)
    image=models.ImageField()
