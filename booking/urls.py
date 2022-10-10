from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('add_booking/', views.add_booking, name='add_booking'),
]
