from django.shortcuts import render
from .models import Recipe

def index(request):
    return render(request, 'homescreen.html')

def recipes(request):
    return render(request, 'recipes.html')

def ingredients(request):
    recipes = []
    for recipe in Recipe.objects.all():
        recipes.append({
            'title': recipe.title,
            'ingredients': recipe.ingredients,
            'directions': recipe.directions,
            'image': recipe.image
        })

    return render(request, 'ingredients.html', {'recipes': recipes})
