from django.shortcuts import render
from django.views import generic
from .models import Patient, Booking
from .forms import BookingForm, PatientForm

# Create your views here.


def home_page(request):
    template = 'booking/home.html'
    context = {}
    return render(request, template, context)


# def base(request):
#     bookings = Booking.objects.all()
#     template = 'booking/base.html'
#     context = {
#         'bookings': bookings,
#     }
#     return render(request, template, context)


def add_patient(request):
    patient_form = PatientForm(request.POST or None)
    if request.method == "POST":
        if patient_form.is_valid():
            patient_form.save()
    template = "booking/new_patient.html"
    context = {
        "patient_form": patient_form,
    }
    return render(request, template, context)


def create_patient(request):
    if request.method == "post":
        forename = request.POST.get("fname")
        surname = request.POST.get("lname")         
        patient.objects.create(forename=forename, surname=surname)
        return render(request, 'patient_booking/')


def book_patient(request):
    if request.methtod == 'POST':
        form = BookingForm()
        context = {
         'form': form
        }

        return render(request, 'patient_booking/base.html', context)
