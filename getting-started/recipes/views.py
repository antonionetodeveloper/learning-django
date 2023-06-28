import json

from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse

from recipes.models import Recipe


def my_view(request):
    return HttpResponse("by default")


def show_all_recipes(request):
    data = Recipe.objects.all().order_by("-id")
    data = serialize("json", data)
    data = json.loads(data)

    return JsonResponse(data, safe=False)


def recipe(request, id):
    data = Recipe.objects.filter(id=id).order_by("-id")
    data = serialize("json", data)
    data = json.loads(data)

    return JsonResponse(data, safe=False)
