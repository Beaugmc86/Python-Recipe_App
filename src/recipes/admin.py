from django.contrib import admin

# Import models
from .models import Recipe

# Register your models here.
admin.site.register(Recipe)
