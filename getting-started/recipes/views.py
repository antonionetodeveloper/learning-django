import json

from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from recipes.models import AuthorForm, Recipe


def show_all_recipes(request):
    data = Recipe.objects.all().order_by("-id")
    data = serialize("json", data)
    data = json.loads(data)

    return JsonResponse(data, safe=False)


def recipe(request, id):
    data = get_object_or_404(Recipe, pk=id, is_published=True)
    data = (serialize("json", [data]),)
    data = json.loads(data)

    return JsonResponse(data, safe=False, status=200)


def category(request, name):
    data = get_list_or_404(
        Recipe.objects.filter(category__name=name, is_published=True).order_by("-id")
    )
    data = serialize("json", data)
    data = json.loads(data)

    return JsonResponse(data, safe=False, status=200)


def author(request, name):
    data = get_list_or_404(
        Recipe.objects.filter(author__name=name, is_published=True).order_by("-id")
    )
    data = serialize("json", data)
    data = json.loads(data)

    return JsonResponse(data, safe=False, status=200)


@csrf_exempt
def add_author(request):
    body = json.loads(request.body)
    if request.method == "POST":
        try:
            data = {"name": body.get("name")}
            serializer = AuthorForm(data=data)
            serializer.save()
            return JsonResponse({"message": "success "}, status=201)

        except Exception:
            return JsonResponse(
                {"message": "Não foi possível adicionar autor."}, status=400
            )

    return JsonResponse({"message": "Method not allowed"}, status=405)
