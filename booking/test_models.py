from django.test import TestCase
from .models import Booking
from .models import Patient


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        booking = Booking.objects.create(_all_='Test Booking')
        self.assertEquals(booking.booked)


    def test_done_defaults_to_false(self):
        patient = Patient.objects.create(_all_='Test Patient')
        self.assertEquals(booking.booked)
