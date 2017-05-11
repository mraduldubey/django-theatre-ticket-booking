from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from allauth.account.signals import user_logged_in, user_signed_up
#from django.core.validators import validate_comma_separated_integer_list
import datetime

# Create your models here.
class Theatre(models.Model):
    city_choice=(
        ('DELHI','Delhi'),
        ('KOLKATA','Kolkata'),
        ('MUMBAI','Mumbai'),
        ('CHENNAI','Chennai'),
        ('BANGALORE','Bangalore'),
        ('HYDERABAD','Hyderabad'),
    )
    name = models.CharField(max_length=50,null=False,default="Waves Cinema")
    city = models.CharField(max_length=9,choices=city_choice,null=False)
    address = models.CharField(max_length=30)
    no_of_screen = models.IntegerField()
    admin_id = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name+"-"+self.address+"-"+self.city


class Movie(models.Model):
    lang_choice = (
        ('ENGLISH', 'English'),
        ('BENGALI', 'Bengali'),
        ('HINDI', 'Hindi'),
        ('TAMIL', 'Tamil'),
        ('TELUGU', 'Telugu'),
    )
    rating_choice = (
        ('U', 'U'),
        ('UA', 'U/A'),
        ('A', 'A'),
        ('R', 'R'),
    )
    name = models.CharField(max_length=20,null=True,blank=True)
    cast = models.CharField(max_length=100,null=True,blank=True)
    director = models.CharField(max_length=20,null=True,blank=True)
    language = models.CharField(max_length=10, choices=lang_choice)
    run_length = models.IntegerField(help_text="Enter run length in minutes",null=True,blank=True)
    certificate = models.CharField(max_length=2, choices=rating_choice)
    popularity_index = models.IntegerField(unique=True, null=True, blank=True)
    trailer = models.URLField(blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='media')

    def __str__(self):
        return self.name


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE,null=True,blank=True)
    screen = models.IntegerField(default=1)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return str(self.movie) + "-" + str(self.theatre) + "-" + str(self.date) + "-" + str(self.time)


class Booking(models.Model):
    payment_choice = (
        ('Credit Card', 'Credit Card'),
    )
    id = models.CharField(primary_key=True, max_length=200)
    timestamp = models.DateTimeField('%Y-%m-%d %H:%M:%S',null=True,blank=True)
    payment_type = models.CharField(max_length=11, choices=payment_choice,default='Credit Card')
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2,null=True,blank=True)
    paid_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING,null=True,blank=True)

    def __str__(self):
        return str(self.id)


class Seat(models.Model):
    seat_choice = (
        ('', 'Select'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Platinum', 'Platinum'),
    )
    no = models.CharField(max_length=3,null=True,blank=False)
    seat_type = models.CharField(max_length=8, choices=seat_choice, blank=False)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('no', 'show')

    def __str__(self):
        return self.no + str(self.show)


class BookedSeat(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('seat', 'booking')

    def __str__(self):
        return str(self.seat) + '|' + str(self.booking)



def show_index(request):
    movie_list = Movie.objects.all().order_by('popularity_index')
    top_movie = Movie.objects.all().order_by('popularity_index')[:3]
    return render(request, 'common/booking.html', {'movie_list': movie_list,'top_movie': top_movie})
