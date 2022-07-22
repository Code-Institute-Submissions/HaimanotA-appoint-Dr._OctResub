from django import forms
from .models import Booking, Patient


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['booking_date', 'booking_id']


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"
