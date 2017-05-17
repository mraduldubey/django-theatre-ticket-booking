from django.contrib.auth.decorators import login_required #the login_required decorator
from django.shortcuts import render,redirect
from .models import *
from django.core.mail import send_mail

from .forms import SeatForm,BookingForm,SelectedSeatForm
import datetime

@login_required
def reserve_seat(request, show_id):
    try:
        show_info = Show.objects.get(pk=show_id)
    except Show.DoesNotExist:
        raise Http404("Page Does Not Exist.")
    form  = SeatForm()
    form2 = SelectedSeatForm()
    context = {'show_info':show_info,'form':form,'form2':form2}

    return render(request,'booking/reserve_seat.html',context)

@login_required
def payment_gateway(request):
    if request.POST:
        seats = request.POST.get('selected_seat')
        seat_type = request.POST.get('seat_type')
        show_id = request.POST.get('show_id')

        show = Show.objects.get(pk=show_id)
        seats = seats.split(',')
        book_seat = []
        for each in seats:
            try:
                #if seat not found in DB
                s = Seat.objects.get(seat_type=seat_type,no=each, show=show)
            except:
                #redirect to seatnotfound.html
                return redirect('booking/seatnotfound.html')

            if Seat.objects.filter(seat_type=seat_type,no=each,show=show):
                s = Seat(no=each,seat_type=seat_type,show=show)
                book_seat.append(s)

        form = BookingForm()

        price_rate = 1000 #Yes.
        ticket_price = price_rate * len(book_seat)

        #Creating the seat string.
        seat_str = ""
        for i in range(len(seats)):
            if i == len(seats)-1:
                seat_str += seats[i]
            else:
                seat_str += seats[i] + ','

        context = {'seats': seat_str,'seat_type':seat_type,'show':show,'form':form,'ticket_price':ticket_price}
        return render(request,'booking/payment_gateway.html',context)
    else:
        return redirect('dashboard.views.home')

def payment_confirmation(request):
	if request.POST:
		show_id = request.POST.get('show_id')
		show = Show.objects.get(pk=show_id)
		seats = request.POST.get('selected_seat')
		seats = seats.split(',')
        seat_type = request.POST.get('seat_type')
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        payment_type = request.POST.get('payment_type')
        paid_amount = request.POST.get('amount')
        paid_by = request.user
        id = str(show) + str(seats) + timestamp
        book = Booking(id=id, timestamp=timestamp, payment_type=payment_type,paid_amount=paid_amount, paid_by=paid_by)
        book.save()

        booked_seat = []
#removed bug of multiple booking of a seat.
        for seat in seats:
            print seat
            s = Seat.objects.get(no=seat, show=show)
            b = Booking.objects.get(pk=id)
            try:
                #if seats not already booked:
                sc = BookedSeat.objects.get(seat=s) #Search only by seat obj
            except:
                #then book them:
                booked = BookedSeat(seat=s, booking=b)
                booked_seat.append(booked)
            else:
                #If already booked, then redirect.
                return redirect('booking/seatconflict.html')
        BookedSeat.objects.bulk_create(booked_seat)
        return render(request, 'booking/payment_confirmation.html')
    #else:
        #return redirect('dashboard.views.home')

def show_index(request):
	movie_list = Movie.objects.all().order_by('popularity_index')
	top_movie = Movie.objects.all().order_by('popularity_index')[:3]

	return render(request, 'common/booking.html', {'movie_list': movie_list,
		'top_movie': top_movie})

def movie_list(request):
	movies = Movie.objects.all().order_by('language')
	movie_list = []
	movie_by_lang = []
	lang = movies[0].language
	for i in range(0, len(movies)):
		if lang != movies[i].language:
			lang = movies[i].language
			movie_list.append(movie_by_lang)
			movie_by_lang = []
		movie_by_lang.append(movies[i])

	movie_list.append(movie_by_lang)

	return render(request, 'movie/movie_list.html', {'movies': movie_list})


def movie_details(request, movie_id):
	try:
		movie_info = Movie.objects.get(pk=movie_id)
		shows = Show.objects.filter(movie=movie_id,
			date=datetime.date.today()).order_by('theatre')
		show_list = []
		show_by_theatre = []
		theatre = shows[0].theatre
		for i in range(0, len(shows)):
			if theatre != shows[i].theatre:
				theatre = shows[i].theatre
				show_list.append(show_by_theatre)
				show_by_theatre = []
			show_by_theatre.append(shows[i])

		show_list.append(show_by_theatre)

	except Movie.DoesNotExist:
		raise Http404("Page does not exist")
	return render(request, 'movie/movie_details.html',
		{'movie_info': movie_info, 'show_list': show_list})


def theatre_list(request):
	theatres = Theatre.objects.all().order_by('city')
	theatre_list = []
	theatre_by_city = []
	city = theatres[0].city
	for i in range(0, len(theatres)):
		if city != theatres[i].city:
			city = theatres[i].city
			theatre_list.append(theatre_by_city)
			theatre_by_city = []
		theatre_by_city.append(theatres[i])

	theatre_list.append(theatre_by_city)

	return render(request, 'theatre/theatre_list.html', {'theatres': theatre_list})


def theatre_details(request, theatre_id):
	try:
		theatre_info = Theatre.objects.get(pk=theatre_id)
		shows = Show.objects.filter(theatre=theatre_id,
			date=datetime.date.today()).order_by('movie')

		show_list = []
		show_by_movie = []
		movie = shows[0].movie
		for i in range(0, len(shows)):
			if movie != shows[i].movie:
				movie = shows[i].movie
				show_list.append(show_by_movie)
				show_by_movie = []
			show_by_movie.append(shows[i])

		show_list.append(show_by_movie)

		print(show_list)

	except Theatre.DoesNotExist:
		raise Http404("Page does not exist")
	return render(request, 'theatre/theatre_details.html',
		{'theatre_info': theatre_info, 'show_list': show_list})
