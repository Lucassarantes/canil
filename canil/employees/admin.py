from django.contrib import admin
from .models import Employee, Role


class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name', 'registry')

admin.site.register(Role)
admin.site.register(Employee, EmployeeAdmin)
