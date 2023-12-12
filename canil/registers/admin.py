from django.contrib import admin

from .models import Employee, Role, Housing, Medicine, Owner, Animal

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name', 'registry')

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'greed', 'owner')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Role)
admin.site.register(Housing)
admin.site.register(Medicine)
admin.site.register(Owner)
admin.site.register(Animal, AnimalAdmin)