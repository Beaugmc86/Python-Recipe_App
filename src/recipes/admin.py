from django.contrib import admin
from .models import Recipe

# Import models
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'cooking_time', 'display_difficulty')
    readonly_fields = ('display_difficulty',)

# Register your models here.
admin.site.register(Recipe, RecipeAdmin)
