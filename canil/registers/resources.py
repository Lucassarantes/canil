from import_export import resources
from .models import Animal, Owner

class AnimalResource(resources.ModelResource):
    class Meta:
        model = Animal
        
    def before_import_row(self, row, **kwargs):
        owner, created = Owner.objects.get_or_create(name = row["owner"],
            phone='123456789',
            email='owner@example.com',
            cpf='12345678901',
            zip='12345678',
            address='123 Main St',
            city='São Paulo',
            state='SP'
        )
        row["owner"] = owner
        # for data in row:
        #     print("data", data)
        #print(row["owner"])