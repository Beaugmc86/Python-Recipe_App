from django.test import TestCase
from .models import Recipe

# Create your tests here.

class RecipeModelTest(TestCase):
    
    # Set up non-modified objects use by all test methods
    def setUpTestData():
        Recipe.objects.create(
            name = 'Tea',
            cooking_time = 5,
            ingredients = "Tea Leaves, Water, Sugar",
        )

    # Test recipe Name
    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)

        # get metadata for 'name' field and use it to query its data
        field_label = recipe._meta.get_field("name").verbose_name
        
        # Compare the value to the expected result
        self.assertEqual(field_label, "name")

    # Test recipe name length
    def test_recipe_name_max_length(self):
        # Get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Get metadata for 'name' field and use it to query its data
        max_length = recipe._meta.get_field("name").max_length

        # Compare the value to the expected result
        self.assertEqual(max_length, 120)

    # Test cooking time
    def test_cooking_time_value(self):
        # Get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Get metadata for 'cooking_time' field and use it to query its data
        cooking_time_value = recipe.cooking_time

        # Compare the value to the expected result
        self.assertIsInstance(cooking_time_value, int)

    # Test ingredients max length
    def test_ingredients_max_length(self):
        # Get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Get metadata for 'ingredients' field and use it to query its data
        max_length = recipe._meta.get_field("ingredients").max_length

        # Compare the value to the expected result
        self.assertEqual(max_length, 400)