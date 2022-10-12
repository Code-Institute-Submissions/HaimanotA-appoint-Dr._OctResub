from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('booking.urls'), name='booking-urls'),
    path('edit/<Booking_id>', edit_booking, name='edit'),
]
