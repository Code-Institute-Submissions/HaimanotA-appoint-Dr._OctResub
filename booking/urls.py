from django.urls import path
from .import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('add_booking/', views.add_booking, name='add_booking'),
    path('edit_booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('manage_bookings/', views.manage_bookings, name='manage_bookings'),
]
