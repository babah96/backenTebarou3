from django.db import models

# Create your models here.
class Urgence(models.Model):
    lantitude= models.DecimalField(max_length=10,max_digits=9, decimal_places=7)
    longitude=models.DecimalField(max_length=10,max_digits=9, decimal_places=7)
    descreption=models.TextField(null=True, blank=True)
    image=models.ImageField()
