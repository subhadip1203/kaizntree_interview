from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator




class Category(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sku = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.CharField(max_length=255, blank=True)
    instock = models.FloatField(validators=[MinValueValidator(0.0)])
    available_stock =  models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f"{self.name} ({self.sku})"
