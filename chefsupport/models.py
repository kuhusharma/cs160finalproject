from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.JSONField(default=list)
    directions = models.JSONField(default=list)
    image = models.URLField(max_length=1000)


