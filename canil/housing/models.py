from django.db import models

class Housing(models.Model):
    registry = models.CharField(max_length = 200) 
    address = models.CharField(max_length = 200)
    vacancies = models.CharField(max_length = 200)

    def __str__(self):
        return self.address