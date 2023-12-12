from django.db import models
from canil.registers.models import Animal, Housing

class HousingManagement(models.Model):
    housing = models.ForeignKey(Housing, on_delete = models.CASCADE)
    last_cleaning = models.DateField()
    next_cleaning = models.DateField()
    
    def __str__(self):
        return self.housing.address
    
    def date_validation(self):
        return self.next_cleaning

class AnimalHealth(models.Model):
    animal = models.ForeignKey(Animal, on_delete = models.CASCADE)
    animal_type = models.CharField(max_length = 200, editable = False)
    animal_greed = models.CharField(max_length = 200, editable = False)
    last_appointment = models.DateField()
    next_appointment = models.DateField()
    diagnosis = models.CharField(max_length = 200)
    appointment_comments = models.TextField()

    def __str__(self):
        return self.animal.name
    
    def save(self, *args, **kwargs):
        selected_animal = self.animal
        if selected_animal:
            self.animal_type = selected_animal.animalType
            self.animal_greed = selected_animal.greed
        super(AnimalHealth, self).save(*args, **kwargs)
        
class Adoption(models.Model):
    animal = models.ForeignKey(Animal, on_delete = models.CASCADE)
    
    next_appointment = models.DateField()
    diagnosis = models.CharField(max_length = 200)
    appointment_comments = models.TextField()

    def __str__(self):
        return self.animal.name
