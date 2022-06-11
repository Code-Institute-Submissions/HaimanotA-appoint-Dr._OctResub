from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Patient(models.Model):
    
    forename = models.CharField(
        verbose_name=('First name'),
        max_length=30,
        blank=False,
        null=False,
    )

    surname = models.CharField(
        verbose_name=('Last name'),
        max_length=30,
        blank=False,
        null=False,
    )

    gender = models.CharField(
        max_length=10,
        verbose_name=('Gender'),
        choices=(
            ('mrs', 'Mrs'),
            ('mr', 'Mr'),
        ),
        blank=False,
        null=False,
    )

    title = models.CharField(
        max_length=10,
        verbose_name=('Title'),
        choices=(
            ('Dr', 'Dr.'),
            ('Prof', 'Prof.'),
        ),
        blank=True,
        null=True,
    )

    booked = models.BooleanField(null=False, blank=False, default=False)

    email = models.EmailField(
        verbose_name=('Email'),
        blank=False,
        null=False,
    )

    phone = models.CharField(
        verbose_name=('Phone'),
        max_length=256,
        blank=True,
    )

    def __str__(self):
        return f"{self.forename} {self.surname}"


class Booking(models.Model):

    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE,
        blank=False,
        null=False
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

    def __str__(self):
        return f"{self.patient.forename} {self.patient.surname} - {self.booking_id}"

