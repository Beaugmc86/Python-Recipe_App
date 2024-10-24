from django.urls import path
from .views import home, RecipeListView, RecipeDetailView

app_name = 'recipes'

urlpatterns = [
    path("", home), # Map the home view to the root URL of the app.
    path('list/', RecipeListView.as_view(), name="list"), # Map the RecipeListView to '/list/', named 'list'
    path("list/<pk>/", RecipeDetailView.as_view(), name="detail"), # Map RecipeDetailView to '/list/<int:pk>/', where 'pk' is a placeholder for the recipe ID, named 'detail'.
]