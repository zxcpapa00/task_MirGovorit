from django.urls import path

from book.views import CreateRecipeAPIView

app_name = 'book'

urlpatterns = [
    path('add_product_to_recipe/', CreateRecipeAPIView.as_view())
]
