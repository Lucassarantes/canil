from django.contrib import admin
from .models import AnimalHealth, HousingManagement

class AnimalHealthAdmin(admin.ModelAdmin):
    readonly_fields = ['animal_type', 'animal_greed']

admin.site.register(HousingManagement)
admin.site.register(AnimalHealth, AnimalHealthAdmin)