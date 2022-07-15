from django.shortcuts import render
from django.views import generic
from .models import Patient, Booking, Specialities

# Create your views here.


def home_page(request):
    bookings = Booking.objects.all()
    template = 'booking/booking.html'
    context = {
        'bookings': bookings,
    }
    return render(request, template, context)
    
def base(request):
    bookings = Booking.objects.all()
    template = 'booking/base.html'
    context = {
        'bookings': bookings,
    }
    return render(request, template, context)