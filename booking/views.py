from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Patient, Booking
from .forms import BookingForm, PatientForm


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
            return redirect(add_patient)
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


def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking_form = BookingForm(request.POST or None, instance=booking)
    if request.method == "POST":
        if booking_form.is_valid():
            booking_form.save()
            messages.success(request, 'Booking edited successfully!')
            return redirect(home_page)
    template = "booking/edit_booking.html"
    context = {
        "booking": booking,
        "booking_form": booking_form,
    }
    return render(request, template, context)


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('manage_bookings')


def manage_bookings(request):
    bookings = Booking.objects.all()
    template = "booking/manage_bookings.html"
    context = {
        "bookings": bookings
    }
    return render(request, template, context)