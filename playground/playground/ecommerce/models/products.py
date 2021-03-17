from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    availability = models.IntegerField()
    image_path = models.ImageField()
