from django.contrib import admin
from .models import Patient, Booking

# Register your models here.

admin.site.register(Patient)
admin.site.register(Booking)
