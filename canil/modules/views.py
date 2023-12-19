from django.shortcuts import render
from canil.registers.models import Animal

def home(request):
    animals = Animal.objects.filter(status='F')
    animal_types = {
        'A': 'Ape',
        'B': 'Bird',
        'C': 'Cat',
        'D': 'Dog',
    }

    animal_data = [(animal, animal_types.get(animal.animal_type, 'Unknown')) for animal in animals]

    return render(request, 'home.html', {'animal_data': animal_data})

