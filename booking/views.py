from django.shortcuts import render
from django.views import generic
from .models import Patient, Booking, Specialities

# Create your views here.


def home_page(request):
    bookings = Booking.objects.all()
    return render(request, 'booking/booking.html')

def base(request):
    bookings = Booking.objects.all()
    return render(request, 'booking/base.html')
