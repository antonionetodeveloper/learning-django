from django.urls import path

from recipes.views import recipe, show_all_recipes

urlpatterns = [
    path("", show_all_recipes, name="all_recipes"),
    path("recipe/<int:id>/", recipe, name="recipe"),
]
