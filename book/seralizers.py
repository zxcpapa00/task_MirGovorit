from rest_framework import serializers

from book.models import RecipeProduct, Product, Recipe


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "count_uses"]


class RecipeSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ["id", "name", "products"]


class RecipeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeProduct
        fields = ["id", "product", "recipe", "weight"]
