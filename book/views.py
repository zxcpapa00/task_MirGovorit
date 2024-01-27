from django.db.models import Q
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response, SimpleTemplateResponse
from rest_framework.views import APIView

from book.models import RecipeProduct, Recipe, Product
from book.seralizers import RecipeProductSerializer, RecipeSerializer, ProductSerializer


class CreateRecipeAPIView(CreateAPIView):
    queryset = RecipeProduct.objects.all()
    serializer_class = RecipeProductSerializer

    def create(self, request, *args, **kwargs):
        recipe_product, created = self.get_queryset().get_or_create(
            recipe=request.data.get('recipe'),
            product=request.data.get('product')
        )
        if not created:
            recipe_product.weight = request.data.get('weight')
            recipe_product.save()

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'error': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)


class RecipeRetrieveAPIView(RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get(self, request, *args, **kwargs):
        for product in self.get_object().products.all():
            product.count_uses += 1
            product.save()
        return super().get(request, *args, **kwargs)


class GetMenuHTMLAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = RecipeSerializer

    def retrieve(self, request, *args, **kwargs):
        product = self.get_object()

        recipe = Recipe.objects.filter(
            (
                    (Q(recipeproduct__product=product) & Q(recipeproduct__weight__lt=10))
                    |
                    ~Q(recipeproduct__product=product)
            )
        )

        return SimpleTemplateResponse(template='menu/menu.html', context={'data': recipe, 'product': product})
