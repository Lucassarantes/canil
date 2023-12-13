from django.db import models
from django.core.exceptions import ValidationError
from canil.registers.models import Animal, Housing

def validate_date_order(model_instance, last_date_field, next_date_field):
    last_date = getattr(model_instance, last_date_field)
    next_date = getattr(model_instance, next_date_field)

    if last_date and next_date and last_date >= next_date:
        raise ValidationError(f"{last_date_field.capitalize()} cannot be greater than or equal to {next_date_field.capitalize()}.")

class HousingManagement(models.Model):
    housing = models.ForeignKey(Housing, on_delete = models.CASCADE)
    last_cleaning = models.DateField(db_column='last_date')
    next_cleaning = models.DateField(db_column='next_date')
    
    def __str__(self):
        return self.housing.address
    
    def save(self, *args, **kwargs):
        validate_date_order(self, 'last_cleaning', 'next_cleaning')
        try:
            super(HousingManagement, self).save(*args, **kwargs)
        except ValidationError as e:
            print(e.message)

class AnimalHealth(models.Model):
    animal = models.ForeignKey(Animal, on_delete = models.CASCADE)
    animal_type = models.CharField(max_length = 200, editable = False)
    animal_greed = models.CharField(max_length = 200, editable = False)
    last_appointment = models.DateField(db_column='last_date')
    next_appointment = models.DateField(db_column='next_date')
    diagnosis = models.CharField(max_length = 200)
    appointment_comments = models.TextField()

    def __str__(self):
        return self.animal.name
    
    
    def save(self, *args, **kwargs):
        selected_animal = self.animal
        if selected_animal:
            self.animal_type = selected_animal.animalType
            self.animal_greed = selected_animal.greed
        validate_date_order(self, 'last_appointment', 'next_appointment')
        try:
            super(AnimalHealth, self).save(*args, **kwargs)
        except ValidationError as e:
            print(e.message)
    
class AnimalsAdoption(models.Model):
    animals = models.ManyToManyField(Animal)
    
    def __str__(self):
        return f"Animals Adoption #{self.id}"
    