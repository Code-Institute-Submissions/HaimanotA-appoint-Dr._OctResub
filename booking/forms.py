from django import forms
from .models import Booking, Patient


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"
