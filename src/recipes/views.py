from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe

# Create your views here.

# View for welcome page
def home(request):
    return render(request, 'recipes/recipes_home.html')

# View recipe list
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipes_list.html'  # specify main recipe list template

# View recipe details
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipes_detail.html'  # specify reciple detail template