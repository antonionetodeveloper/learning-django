from django.db import models
from django.forms import ModelForm


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=65)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=65)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ["name"]


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=65, unique=True)
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=255)
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to="recipes/covers/%Y/%m/%d/")
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
