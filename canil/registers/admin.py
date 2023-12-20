from django.contrib import admin
from django.http import JsonResponse
import json

from .models import Employee, Role, Housing, Medicine, Owner, Animal
from .forms import EmployeeFormAdmin, AnimalImportForm

class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeFormAdmin
    list_display=('name', 'registry')
    class Media:
        js = (
            '../static/jquery.mask.min.js',
            '../static/custom.js'
        )

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'owner')
    
    form = AnimalImportForm

    def save_model(self, request, obj, form, change):
        if 'json_file' in request.FILES:
            uploaded_file = request.FILES['json_file']
            content = uploaded_file.read()
            try:
                animals_data = json.loads(content)
                created_animals = []

                for animal_data in animals_data:
                    owner_name = animal_data.get('human_owner')
                    
                    owner, created = Owner.objects.get_or_create(name='Lucas')
                    print(animal_data.get('animal_type'))
                    mapped_data = {
                        'animal_type': animal_data.get('animal_type'), 
                        'breed': animal_data.get('breed'),
                        'name': animal_data.get('name'),
                        'age': 5,
                        'size': animal_data.get('size'),
                        'gender': animal_data.get('gender'),
                        'owner': owner,
                        'status': animal_data.get('status')
                    }
                    print(mapped_data)

                    created_animal = Animal.objects.create(**mapped_data)
                    created_animals.append(created_animal)

                # Print or log the list of created animals
                print("Animals created:", created_animals)

                self.message_user(request, 'Animals imported successfully')
            except json.JSONDecodeError as e:
                self.message_user(request, f'Error decoding JSON file: {e}', level=admin.ERROR)
        else:
            super().save_model(request, obj, form, change)

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Role)
admin.site.register(Housing)
admin.site.register(Medicine)
admin.site.register(Owner)
admin.site.register(Animal, AnimalAdmin)