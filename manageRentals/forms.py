from django import forms
from manageRentals.models import rental

class rentalForm(forms.ModelForm):
    class Meta:
        model= rental
        fields = ['isbn','userID', 'rentDate','returnDate']
      