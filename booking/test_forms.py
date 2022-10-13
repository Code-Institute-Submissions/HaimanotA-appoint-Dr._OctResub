from django.test import TestCase
from .forms import BookingForm


class TestItemForm(TestCase):

    def test_booking_name_is_required(self):
        form = BookingForm({'-all_': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('_all_', form.errors.keys())
        self.assertEqual(form.errors['_all_'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = BookingForm({'_all_', 'booked'})
        self.assertTrue(form.is_valid)

    def test_fields_are_explicit_in_form_metaclass(self):
        form = BookingForm()
        self.assertEqual(form.Meta.fields, ['all', 'booked'])
