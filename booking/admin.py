from django.contrib import admin
from .models import Patient, Booking, Specialities, AvailableHour
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Patient)
admin.site.register(Booking)
admin.site.register(Specialities)
admin.site.register(AvailableHour)
