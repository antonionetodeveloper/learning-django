from django.urls import path

from recipes.views import my_view, show_all_recipes

urlpatterns = [
    path("", my_view, name="home"),
    path("about/", my_view, name="about"),
    path("all-recipes/", show_all_recipes, name="all_recipes"),
]
