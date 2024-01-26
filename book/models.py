from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256)
    count_uses = models.SmallIntegerField()

    def __str__(self):
        return self.name


class RecipeProduct(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    weight = models.SmallIntegerField()

    def __str__(self):
        return f'{self.product} {self.weight}'


class Recipe(models.Model):
    name = models.CharField(max_length=512)
    products = models.ManyToManyField(to=RecipeProduct, related_name='where_uses')

    def __str__(self):
        return self.name
