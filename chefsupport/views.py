from django.shortcuts import render
from .models import Recipe

def index(request):
    return render(request, 'homescreen.html')

def recipes(request):
    return render(request, 'recipes.html')

def ingredients(request):
    recipes = Recipe.objects.all()
    return render(request, 'ingredients.html', {'recipes': recipes})
