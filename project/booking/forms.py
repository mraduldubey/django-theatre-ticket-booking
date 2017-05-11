from django import forms
from .models import Seat, Booking

class SeatForm(forms.ModelForm):
    class Meta:
        model = Seat
        fields = ('seat_type',)

class SelectedSeatForm(forms.Form):
    selected_seat = forms.CharField(required=True,max_length=10,help_text='Seat No seperated by ,')

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('payment_type',)
