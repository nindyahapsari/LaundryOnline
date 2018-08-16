from django import forms
from .models import Laundry


class LaundryForms(forms.ModelForm):
    """Form for the laundry form in Home page"""

    class Meta:
        model = Laundry
        fields = [
            'name',
            'location',
            'postcode',
            'laundryweight',
            'description'
            ]
