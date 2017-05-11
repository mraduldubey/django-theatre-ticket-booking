from django.contrib import admin

# Register your models here.
from .models import Booking,Movie,Show,Seat,BookedSeat,Theatre

class BookingAdmin(admin.ModelAdmin):
	class Meta:
		model = Booking

admin.site.register(Booking,BookingAdmin)

class ShowAdmin(admin.ModelAdmin):
	class Meta:
		model = Show

admin.site.register(Show,ShowAdmin)

class MovieAdmin(admin.ModelAdmin):
	class Meta:
		model = Movie

admin.site.register(Movie,MovieAdmin)

class SeatAdmin(admin.ModelAdmin):
	class Meta:
		model = Seat
admin.site.register(Seat,SeatAdmin)

class BookedSeatAdmin(admin.ModelAdmin):
	class Meta:
		model = BookedSeat

admin.site.register(BookedSeat,BookedSeatAdmin)

class TheatreAdmin(admin.ModelAdmin):
	class Meta:
		model = Theatre

admin.site.register(Theatre,TheatreAdmin)
