from django.db import models
from owners.models import Owner
from django.contrib import admin

class Animal(models.Model):
    animalType = models.CharField(max_length=200)
    greed = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=200)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    status = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"
