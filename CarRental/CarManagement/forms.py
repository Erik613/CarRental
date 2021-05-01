from django import forms
from CarManagement.models import verhicle_types
from CarManagement.models import Car

class CarEntryForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        labels = {'brand': 'Marke', 'model_name': 'Modell', 'license_plate': 'Nummernschild', 'seats': 'Sitzplätze', 'km_age': 'Kilometerstand',
                'construction_date': 'Baujahr', 'verhicle_type': 'Fahrzeugtyp', 'is_automatic': 'Automatik', 'reserved': 'Reserviert'}