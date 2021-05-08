from django.db import models

# Create your models here.
class reg(models.Model):
    Username=models.CharField(max_length=100 ,default="")
    email=models.CharField(max_length=200 ,default="")

