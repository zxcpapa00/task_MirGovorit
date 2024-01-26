from django.contrib import admin
from book.models import Product, RecipeProduct, Recipe


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass


@admin.register(RecipeProduct)
class RecipeProductAdmin(admin.ModelAdmin):
    pass
