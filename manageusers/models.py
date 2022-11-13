from django.db import models
import datetime
# from django.contrib.auth.models import User,Group
from django.contrib.auth.models import AbstractUser
# pip install django-rest-knox


# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_simpleUser = models.BooleanField(default=False)
    phone = models.CharField(max_length=10, null=True)
    blood_type = models.CharField(max_length=3, null=True)
    weight = models.IntegerField( null=True)
    height = models.IntegerField( null=True)
    birth = models.DateField( null=True)
    age = models.IntegerField( null=True)

    gender = models.CharField(max_length=1, default="M")

    def get_age(self, b):
        return int((datetime.date.today() - datetime.datetime.strptime(b, "%Y-%m-%d").date()).days / 365.25)
