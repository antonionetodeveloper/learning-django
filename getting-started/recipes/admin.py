from django.contrib import admin

from .models import Author, Category, Recipe


class CategoryAdmin(admin.ModelAdmin):
    ...


class AuthorAdmin(admin.ModelAdmin):
    ...


class RecipeAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Recipe, RecipeAdmin)
