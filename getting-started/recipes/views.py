import json

from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse

from .models import Recipe


def my_view(request):
    return HttpResponse("by default")


def show_all_recipes(request):
    """
    print("-=" * 50)
    print("-=" * 50)
    test_data = Recipe.objects.all()
    for recipe in test_data:
        for field in recipe._meta.fields:
            print(f"{field.name}: {getattr(recipe, field.name)}")
    print("-=" * 50)
    print("-=" * 50)
    """

    data = serialize("json", Recipe.objects.all())
    data = json.loads(data)
    return JsonResponse(data, safe=False)
