from django import forms
from .models import Parcel

class AddParcelForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields = ['departure_address', 'arrival_address', 'weight']