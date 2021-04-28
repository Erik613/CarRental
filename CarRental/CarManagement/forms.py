from django import forms
from CarManagement.models import verhicle_types
from CarManagement.models import Car

class CarEntryForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        labels = {'brand': 'Marke', 'model_name': 'Modell', 'license_plate': 'Nummernschild', 'seats': 'Sitzplätze', 'km_age': 'Kilometerstand',
        'construction_date': 'Baujahr', 'verhicle_type': 'Fahrzeugtyp', 'is_automatic': 'Automatik', 'reserved': 'Reserviert'}
        '''
        fields = ['brand', 'model_name', 'license_plate', 'seats', 'km_age',
        'construction_date', 'vehicle_type', 'is_automatic', 'reserved']
        '''

    '''
    brand = forms.CharField(label='Marke', max_length=100)
    model_name = forms.CharField(label='Modell', max_length=250)
    license_plate = forms.CharField(label='Nummernschild', max_length=50)
    seats = forms.IntegerField(label='Sitzplätze', min_value=2, max_value=50)
    km_age = forms.IntegerField(label='Kilometerstand', min_value=0, max_value=500000)
    construction_date = forms.DateTimeField(label='Baujahr', input_formats='%y')
    verhicle_type = forms.ChoiceField(label='Fahrzeugtyp', choices=verhicle_types)
    is_automatic = forms.BooleanField(label='Automatik', required=True)
    reserved = forms.BooleanField(label='Reserviert', required=True)
    '''