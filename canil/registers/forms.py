from django import forms
from .models import Employee, Animal

class EmployeeFormAdmin(forms.ModelForm):
    class Meta:
        model = Employee
        fields  = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['zip'].widget.attrs['class'] = 'mask_zip'
        #: '00000000'"
        self.fields['phone'].widget.attrs['class'] = 'mask_phone'
        #: '11963001172'"

class AnimalImportForm(forms.ModelForm):
    json_file = forms.FileField(label='Upload JSON File')

    class Meta:
        model = Animal
        fields = '__all__'