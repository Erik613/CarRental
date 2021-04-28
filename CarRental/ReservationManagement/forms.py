from django import forms
from ReservationManagement.models import Reservation
from CustomerManagement.models import Customer
from CarManagement.models import Car
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Q, Exists, OuterRef, F
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

    start_date = forms.DateField(widget=DateInput(), label='Von',
                                 validators=[MinValueValidator(datetime.date.today(),
                                                               message='Datum muss mind. der ' + str(
                                                                   datetime.date.today()) + ' sein')])

    end_date = forms.DateField(widget=DateInput(), label='Bis',
                               validators=[MinValueValidator(datetime.date.today(),
                                                             message='Datum muss mind. der ' + str(
                                                                 datetime.date.today()) + ' sein')])

    id_car = forms.ModelChoiceField(label='Auto',
                                    queryset=Car.objects.filter(
                                        ~Exists(Reservation.objects.filter(id_car=OuterRef('pk'))) |
                                        Q(reservation__end_date__lt=datetime.date.today())))

    id_customer = forms.ModelChoiceField(label="Kunde",
                                         queryset=Customer.objects.filter(
                                             ~Exists(Reservation.objects.filter(id_customer=OuterRef('pk'))) |
                                             Q(reservation__end_date__lt=datetime.date.today())))

    def clean(self):
        cleaned_data = super(ReservationForm, self).clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if start_date > end_date:
                raise ValidationError('Startdatum muss vor Enddatum liegen')

