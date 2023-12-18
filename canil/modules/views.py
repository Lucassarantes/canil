from django.shortcuts import render
from canil.registers.models import Animal

def home(request):
    animals = Animal.objects.filter(status = 'F')
    allAnimals = Animal.objects.all()
    print(allAnimals[0].status)
    return render(request, 'home.html', {'animals': animals})