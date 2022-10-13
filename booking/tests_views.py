from django.test import TestCase
from .models import Item

# Create your tests here.
class TestViews(TestCase):

    def test_get_new_booking_page(self):
        response = self.client.get('/new_booking')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/new_booking.html')
    
    
    def test_edit_booking_page(self):
        response = self.client.get('/edit_booking')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/new_booking.html')

    def test_can_toggle_booking(self):
        Booking = Booking.objects.create(name='Test Booking')
        response = self.client.get(f'/edit/{Booking.id}')
        self.assertRedirects(response, '/')
        updated_booking = Booking.objects.get(id=Bookig.id)
        self.assertTemplateUsed(response, 'booking/edit_booking.html')

    def test__can_delete_booking(self):
        Booking = Booking.objects.create(name='Test Booking', done=True)
        response = self.client.get(f'/delete/{Booking.id}')
        self.assertRedirects(response, '/')
        existing_bookings = Booking.objects.filter(id=Booking.id)
        self.assertRedirects(response, '/')
        