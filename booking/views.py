from django.shortcuts import render, redirect, get_object_or_404
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


def edit_booking(request, Booking_id):
    booking = get_object_or_404(Booking)
    if request.method == "POST":
       if booking_form.is_valid():
        booking_form.save()
        messages.success(request, 'booking edited successfully!')
    return redirect(home_page)
    template = "booking/new_booking.html"
    context = {
        "booking_form": booking_form
    }
    return render(request, 'booking/edit_booking.html', context)


def toggle_booking(request, toggle_id):
        booking = get_object_or_404(Booking, id=booking_id)
        booking.done = not booking.done
        booking.save()
        return redirect('add_patient')


def delete_booking(request, toggle_id):
        booking = get_object_or_404(Booking, id=booking_id)
        booking.delete()
        return redirect('add_patient')