from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='homescreen'),
    path('recipes', views.recipes, name='recipes'),
    path('ingredients', views.ingredients, name='ingredients'),
]