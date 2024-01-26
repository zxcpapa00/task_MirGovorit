from django.urls import path

from book.views import CreateRecipeAPIView, RecipeRetrieveAPIView

app_name = 'book'

urlpatterns = [
    path('add_product_to_recipe/', CreateRecipeAPIView.as_view()),
    path('cook_recipe/<int:pk>', RecipeRetrieveAPIView.as_view())
]
