from django.db import models

# Create your models here.
class Animal(models.Model);
    type = models.CharField(max_length=200)
	greed = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	age = models.IntegerField()
	gender = models.CharField(max_length=200)
	owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    status = models.CharField(max_length=200)
	entrada = models.CharField(max_length=200)
	saída = models.CharField(max_length=200)

class AnimalInline(admin.TabularInline):
    model = Animal
    extra = 0
