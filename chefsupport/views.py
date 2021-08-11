from django.shortcuts import render
from .models import Recipe

def index(request):
    return render(request, 'homescreen.html')

def recipes(request):
    results = Recipe.objects.all()
    recipes = []
    recipes.append(results[6])
    recipes.append(results[7])
    recipes.append(results[11])
    recipes.append(results[15])
    return render(request, 'recipes.html', {'recipes': recipes})

def ingredients(request):
    recipes = Recipe.objects.all()
    return render(request, 'ingredients.html', {'recipes': recipes})
