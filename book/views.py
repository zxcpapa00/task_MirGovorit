from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from book.models import RecipeProduct
from book.seralizers import RecipeProductSerializer


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
        return Response(serializer.data)

        # return Response({'error': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)
