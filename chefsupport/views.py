from django.shortcuts import render

def index(request):
    return render(request, 'homescreen.html')

def recipes(request):
    return render(request, 'recipes.html')

def ingredients(request):
    return render(request, 'ingredients.html')
