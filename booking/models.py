from django.db import models
# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    booked = models.BooleanField(null=False, blank=False, default=False)

class Booking(models.Model):
    gender = models.CharField(
        max_length=10,
        verbose_name=('Gender'),
        choices=(
            ('mrs', 'Mrs'),
            ('mr', 'Mr'),
        ),
        blank=True,
    )

    title = models.CharField(
        max_length=10,
        verbose_name=('Title'),
        choices=(
            ('Dr', 'Dr.'),
            ('Prof', 'Prof.'),
        ),
        blank=True,
    )

    forename = models.CharField(
        verbose_name=('First name'),
        max_length=20,
        blank=True,
    )

    surname = models.CharField(
        verbose_name=('Last name'),
        max_length=20,
        blank=True,
    )

    email = models.EmailField(
        verbose_name=('Email'),
        blank=True,
    )

    phone = models.CharField(
        verbose_name=('Phone'),
        max_length=256,
        blank=True,
    )

    creation_date = models.DateTimeField(
        verbose_name=('Creation date'),
        auto_now_add=True,
    )

    booking_id = models.CharField(
        max_length=100,
        verbose_name=('Booking ID'),
        blank=True,
    )

