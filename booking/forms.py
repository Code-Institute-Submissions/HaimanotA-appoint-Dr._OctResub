from django import forms
from .models import Booking, Patient


class DateInput(forms.DateInput):
    input_type = "date"


class TimeInput(forms.TimeInput):
    input_type = "time"


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
        widgets = {
            "booking_date": DateInput(),
            "booking_time": TimeInput(),
        }


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"
