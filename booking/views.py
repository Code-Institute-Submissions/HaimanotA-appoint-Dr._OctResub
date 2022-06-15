from django.shortcuts import render
from django.views import generic
from .models import Patient

# Create your views here.


def home_page(request):
    return render(request, 'booking/booking.html')
