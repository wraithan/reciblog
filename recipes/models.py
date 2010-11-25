from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=256)
    source = models.CharField(max_length=256)
