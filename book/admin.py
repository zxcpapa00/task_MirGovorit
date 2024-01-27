from django.contrib import admin
from book.models import Product, RecipeProduct, Recipe


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "count_uses"]
    fields = ["name", "count_uses"]


class RecipeProductInline(admin.TabularInline):
    model = RecipeProduct
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeProductInline]


@admin.register(RecipeProduct)
class RecipeProductAdmin(admin.ModelAdmin):
    pass
