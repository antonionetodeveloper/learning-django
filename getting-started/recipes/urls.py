from django.urls import path

from recipes.views import add_author, author, category, recipe, show_all_recipes

urlpatterns = [
    path("", show_all_recipes, name="all_recipes"),
    path("recipe/<int:id>/", recipe, name="recipe"),
    path("category/<str:name>/", category, name="category"),
    path("author/<str:name>/", author, name="author"),
    path("author/add", add_author, name="add_author"),
]
