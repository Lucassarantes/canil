from django.db import models
from django.contrib import admin

class Role(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"{self.id} - {self.name}"

class Employee(models.Model):
    registry = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    cpf = models.CharField(max_length=12)
    zip = models.IntegerField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Housing(models.Model):
    registry = models.CharField(max_length = 200) 
    address = models.CharField(max_length = 200)
    vacancies = models.CharField(max_length = 200)

    def __str__(self):
        return self.address
    
class Medicine(models.Model):
    code = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)
    quantity = models.IntegerField()

    def __str__ (self):
        return self.name

class Owner(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    cpf = models.CharField(max_length=12)
    zip = models.IntegerField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Animal(models.Model):
    animalType = models.CharField(max_length=200)
    greed = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    size = models.CharField(max_length = 200)
    gender = models.CharField(max_length=200)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    status = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"