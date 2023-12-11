from django.contrib import admin
from .models import AnimalHealth, HousingManagement

admin.site.register(HousingManagement)
admin.site.register(AnimalHealth)