from rest_framework import serializers

from book.models import RecipeProduct


class RecipeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeProduct
        fields = ["id", "product", "recipe", "weight"]
