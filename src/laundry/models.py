from django.db import models

# Create your models here.

class Laundry(models.Model):
    """Form models for the DB. It has to be migrate to the DB to see it"""

    name            = models.CharField(max_length=120)
    location        = models.CharField(max_length=60)
    postcode        = models.IntegerField(blank=True)
    laundryweight   = models.IntegerField(blank=True, help_text='weight in KG')
    description     = models.TextField(help_text='For important message or pick up time')

    def __str__(self):
        return self.name
