from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.IntegerField(help_text="in minutes")
    ingredients = models.CharField(
        max_length=400,
        help_text="Enter ingredients, separated by commas"
        )
    notes = models.TextField(default="If you'd like to add a description or notes for your recipe, add them here!")
    pic = models.ImageField(upload_to='recipes', default='no_picture.png')

    def calculate_difficulty(self):
        ingredients = [i.strip() for i in self.ingredients.split(",")]
        if self.cooking_time < 10 and len(ingredients) < 4:
            return 'Easy'
        elif self.cooking_time < 10 and len(ingredients) >= 4:
            return 'Medium'
        elif self.cooking_time >= 10 and len(ingredients) < 4:
            return 'Intermediate'
        else:
            return 'Hard'
    
    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
       return reverse ('recipes:detail', kwargs={'pk': self.pk})