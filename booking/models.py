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
    """Booking model - about the booking"""
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    
    booking_date = models.DateField(
        verbose_name=('booking date'),
        null=True,
    )

appointmenttime  = models.CharField(
        max_length=20,
        verbose_name=('Appointmenttime'),
        choices=(
            ('Morning-1', '8-9'),
            ('Morning-2', '10-11'),
            ('Afternoon-1', '10-11'),
            ('Afternoon-2', '10-11'),
        ),
            blank=False,
            null=True,
    )


booking_id = models.CharField(
        max_length=100,
        verbose_name=('Booking ID'),
        blank=True,
    )

def __str__(self):
        return f"{self.booking_id} - {self.patient.forename} {self.patient.surname} {self.patient.gender} {self.creation_date}{self.appointmenttime}"

class Specialities(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    book = models.BooleanField(null=False, blank=False)

    def __str__(self):
        return self.name

DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)


class WeekDay(models.Model):
    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="weekday"
    )
    weekday = models.IntegerField(choices=DAYS_OF_WEEK)

    
class AvailableHour(models.Model):
    weekday = models.ForeignKey(
        WeekDay,
        on_delete=models.CASCADE,
        related_name="available_hour"
    )
    from_hour = models.TimeField()
    to_hour = models.TimeField()
    