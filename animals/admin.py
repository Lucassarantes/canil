from django.contrib import admin
from .models import Animal

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'greed', 'owner')

admin.site.register(Animal, AnimalAdmin)

