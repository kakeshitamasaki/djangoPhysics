from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    subname = models.CharField(max_length=100,blank=True,null=True)
    desc = models.CharField(max_length=100,blank=True,null=True)
    