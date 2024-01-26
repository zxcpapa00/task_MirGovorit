from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256)
    count_uses = models.SmallIntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=512)
    products = models.ManyToManyField(to=Product, through="RecipeProduct")

    def __str__(self):
        return self.name


class RecipeProduct(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    recipe = models.ForeignKey(to=Recipe, on_delete=models.CASCADE, null=True)
    weight = models.SmallIntegerField()

    def __str__(self):
        return f'{self.product} {self.weight}'
