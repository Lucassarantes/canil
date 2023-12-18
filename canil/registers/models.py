from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, Group
import requests

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
    zip = models.CharField(max_length=8)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200, default = 'São Paulo')
    state = models.CharField(max_length=2, default = 'SP')  

    def fill_address_details(self):
        print(self.zip)
        api_url = f'https://brasilapi.com.br/api/cep/v2/02271140'
        response = requests.get(api_url)
        print(response)
        if response.status_code == 200:
            data = response.json()

            self.address = data.get('street', '')
            self.city = data.get('city', '')
            self.state = data.get('state', '')

    
    def __str__(self):
        return self.name
    
    def save(self):
        self.fill_address_details()
        first_name = self.name.split(' ')[0]
        try:
            user = User.objects.filter(username=usernamegen).first()

            if user is not None:
                print("User already exists 1")
            else:
                user = User.objects.create_user(self.cpf.replace("-", "_"), self.email, self.cpf)
                user.is_staff = True
                user.save()
                role_name = str(self.role).split('- ')[1]
                group = Group.objects.get(name=role_name)
                user.groups.add(group)
        except Exception as e:
            print(f"Error: {e}")
            print("User creation failed")
                
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
    cpf = models.CharField(max_length=14)
    zip = models.CharField(max_length=8, default='00000000')
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200, default = 'São Paulo')
    state = models.CharField(max_length=2, default = 'SP')
    
    def fill_address_details(self):
        print(self.zip)
        api_url = f'https://brasilapi.com.br/api/cep/v2/{self.zip}'
        response = requests.get(api_url)
        
        print(response)

        if response.status_code == 200:
            data = response.json()

            self.address = data.get('street', '')
            self.city = data.get('city', '')
            self.state = data.get('state', '')

    def __str__(self):
        return self.name
    
    def save(self):
        self.fill_address_details()
        super(Owner, self).save()


class Animal(models.Model):
    animal_type = models.CharField(max_length = 1, choices = ANIMAL_TYPE_CHOICES, default = 'D')
    greed = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    size = models.CharField(max_length = 1, choices = ANIMAL_SIZE_CHOICES, default = 'S')
    gender = models.CharField(max_length = 1, choices = ANIMAL_GENDER_CHOICES, default = 'M')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    status = models.CharField(max_length = 1, choices = ANIMAL_STATUS_CHOICES, default = 'F')

    def __str__(self):
        return f"{self.name}"