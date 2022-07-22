from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Patient(models.Model):
    """Patient model - who made a reservation"""
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
            ('Male','Male'),
            ('Female','Female'),
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
            ('Mr', 'Mr.'),
            ('Mrs', 'Mrs.'),
            ('Ms', 'Ms.'),
        ),
        blank=True,
        null=True,
    )
    
    email = models.EmailField(   
        max_length=30,
        verbose_name=('Email'),
        blank=False,
        null=False,
    )

    phone = models.CharField(
        verbose_name=('Phone'),
        max_length=20,
        blank=True,
    )


    def __str__(self):
        return f"{self.forename} {self.surname}"

class Booking(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

    booking_date = models.DateField(
        verbose_name=('booking date'),
        null=True,
    )

    booking_id = models.CharField(
        max_length=100,
        verbose_name=('Booking Id'),
        blank=True,
    )


def __str__(self):
        return f"{self.patient.surname}"
        