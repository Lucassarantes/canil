from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, Group

# Animals choices
ANIMAL_TYPE_CHOICES = (
    ('A', 'Ape'),
    ('B', 'Bird'),
    ('C', 'Cat'),
    ('D', 'Dog'),
)
ANIMAL_SIZE_CHOICES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('B', 'Big'),
)
ANIMAL_GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)
ANIMAL_STATUS_CHOICES = (
    ('F', 'Free'),
    ('H', 'Has Owner'),
    ('I', 'Ill'),
    ('D', 'Dead')
)

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
    cpf = models.CharField(max_length=14)
    zip = models.IntegerField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200, default = 'São Paulo')
    state = models.CharField(max_length=2, default = 'SP')
    
    def __str__(self):
        return self.name
    
    def gen_pass(self):
        name = self.name.split()
        return name[0] +'_'+ self.cpf
    
    def save(self):
        first_name = self.name.split(' ')[0]
        user = User.objects.create_user(first_name, self.email, self.gen_pass())
        user.is_staff = True
        user.save()
        group = Group.objects.get(name = 'Recepcionist')
        user.groups.add(group)
        
        super(Employee, self).save()

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
    city = models.CharField(max_length=200, default = 'São Paulo')
    state = models.CharField(max_length=2, default = 'SP')

    def __str__(self):
        return self.name


class Animal(models.Model):
    animal_type = models.CharField(max_length = 1, choices = ANIMAL_TYPE_CHOICES, default = 'D')
    greed = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    size = models.CharField(max_length = 1, choices = ANIMAL_SIZE_CHOICES, default = 'S')
    gender = models.CharField(max_length = 1, choices = ANIMAL_GENDER_CHOICES, default = 'M')
    # default_owner = Owner.objects.get_or_create(name='no_owner')[0]
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    status = models.CharField(max_length = 1, choices = ANIMAL_STATUS_CHOICES, default = 'F')

    def __str__(self):
        return f"{self.name}"