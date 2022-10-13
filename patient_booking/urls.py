from django.contrib import admin
from django.urls import path, include
from booking.views import add_booking, add_patient, edit_booking
from booking import views     #added

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('booking.urls'), name='booking-urls'),
]
