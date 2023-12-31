from django.contrib import admin
from .models import AnimalHealth, HousingManagement
from canil.registers.models import Animal

class AnimalHealthAdmin(admin.ModelAdmin):
    readonly_fields = ['animal_type', 'animal_greed']
    
    
    def display_animals(self, obj):
        return "\n".join([f"{animal.id} | {animal.name} | {animal.animal_type} | {animal.greed} | {animal.status}" for animal in obj.animals.all()])
    
    display_animals.short_description = 'id | name | type | greed | status'
    
    

admin.site.register(HousingManagement)
admin.site.register(AnimalHealth, AnimalHealthAdmin)