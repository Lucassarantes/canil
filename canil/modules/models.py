from django.db import models
from canil.housing.models import Housing
from animals.models import Animal

class HousingManagement(models.Model):
    housing = models.ForeignKey(Housing, on_delete = models.CASCADE)
    last_cleaning = models.DateField()
    next_cleaning = models.DateField()

class AnimalHealth(models.Model):
    animal = models.ForeignKey(Animal, on_delete = models.CASCADE)
    last_appointment = models.DateField()
    next_appointment = models.DateField()
    diagnosis = models.CharField(max_length = 200)
    appointment_comments = models.TextField()

