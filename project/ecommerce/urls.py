"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static #for static files on local server.
from django.conf.urls import include
from django.views.generic import TemplateView

from dashboard import views as dash_views
from contact import views as cont_views
from checkout import views as check_views
from booking import views as booking_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', dash_views.home, name='home'),
    url(r'^dashboard/$', dash_views.dashboard,name='dashboard'),
    url(r'^contact/$', cont_views.contact,name='contact'),
    url(r'^accounts/', include('allauth.urls')),
    #url(r'^booking/$', booking_views.movie_list, name='movie_list'),
    url(r'^booking/$', booking_views.show_index,name='booking'),
    url(r'^checkout/$', check_views.checkout,name='checkout'),
    url(r'^booking/(?P<movie_id>\d+)/$', booking_views.movie_details, name='movie_details'),
    url(r'^booking/seatchoice/(?P<show_id>\d+)/$', booking_views.reserve_seat, name='reserve_seat'),
    url(r'^booking/payment/$', booking_views.payment_gateway, name='payment_gateway'),
    url(r'^booking/payment_confirmation/$', booking_views.payment_confirmation, name='payment_confirmation'),
    #Hard Coded templates i.e. without views.
    url(r'^booking/payment/booking/seatnotfound.html$', TemplateView.as_view(template_name="booking/seatnotfound.html"), name='seatnotfound'),
    url(r'^booking/payment_confirmation/booking/seatconflict.html$', TemplateView.as_view(template_name="booking/seatconflict.html"), name='seatconflict'),


]



if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #all values set in settings.py
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
