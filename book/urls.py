from django.urls import path

from book.views import CreateRecipeAPIView, RecipeRetrieveAPIView, GetMenuHTMLAPIView

app_name = 'book'

urlpatterns = [
    path('add_product_to_recipe/',
         CreateRecipeAPIView.as_view(),
         name='add_product_to_recipe'
         ),
    path('cook_recipe/<int:pk>',
         RecipeRetrieveAPIView.as_view(),
         name='cook_recipe'
         ),
    path(
        'show_recipes_without_product/<int:pk>',
        GetMenuHTMLAPIView.as_view(),
        name='show_recipes_without_product'
    )
]
