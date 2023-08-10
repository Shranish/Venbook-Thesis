from django.urls import include, path

from . import views


app_name='venue'


urlpatterns= [
    path('venuedisplay', views.VenueDisplay, name='VenueDisplay'),
    path('dashboard/<int:id>', views.VenueEdit, name='VenueEdit'),
    path('updatevenueprice/', views.VenuePriceUpdate, name='VenuePriceUpdate'),
    path('updatevenuedesc/<int:id>', views.VenueDescUpdate, name='VenueDescUpdate'),
    path('venuedetail/<int:id>',views.VenueDetail,name="VenueDetail"),
    path('booking-request/',views.BookingRequest,name="BookingRequest"),
]



