from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver

from book.models import RecipeProduct


# @receiver(pre_save, sender=RecipeProduct)
# def check_unique_recipe_product(sender, instance, **kwargs):
#     existing_product = RecipeProduct.objects.filter(recipe=instance.recipe, product=instance.product)
#     if existing_product.exists() and not instance.pk:
#         existing_product.first().weight = instance.weight
#         existing_product.first().save()
