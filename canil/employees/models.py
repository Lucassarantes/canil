from django.db import models

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

