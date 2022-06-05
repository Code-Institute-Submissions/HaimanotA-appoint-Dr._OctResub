from django.db import models

# Create your models here.


class patient(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    booked = models.BooleanField(null=False, blank=False, default=False)