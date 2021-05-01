from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        labels = {'first_name': 'Vorname', 'last_name': 'Nachname', 'birth_date': 'Geburtsdatum', 'residence_street': 'Straße', 'residence_number': 'Hausnummer',
                'residence_city': 'Stadt'}
