from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages 
from .models import Patient, Booking
from .forms import BookingForm, PatientForm

# Create your views here.


def home_page(request):
    template = 'booking/home.html'
    context = {}
    return render(request, template, context)


def add_patient(request):
    patient_form = PatientForm(request.POST or None)
    if request.method == "POST":
        if patient_form.is_valid():
            patient_form.save()
            messages.success(request, 'patient addded successfully!')
            return redirect(home_page)
    template = "booking/new_patient.html"
    context = {
        "patient_form": patient_form,
    }
    return render(request, template, context)


def add_booking(request):
    booking_form = BookingForm(request.POST or None)
    if request.method == "POST":
        if booking_form.is_valid():
            booking_form.save()
            messages.success(request, 'booking addded successfully!')
            return redirect(home_page)
    template = "booking/new_booking.html"
    context = {
        "booking_form": booking_form,
    }
    return render(request, template, context)
