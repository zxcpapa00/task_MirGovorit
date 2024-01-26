from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256)
    count_uses = models.SmallIntegerField()

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=512)
    products = models.ManyToManyField(to=Product, related_name='where_uses')

    def __str__(self):
        return self.name
