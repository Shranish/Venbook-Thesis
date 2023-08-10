from django.urls import path

from . import views

app_name='accounts'

urlpatterns= [
    path('registerAsUser', views.registerAsUser, name='registerAsUser'),
    path('loginAsUser', views.loginAsUser, name='loginAsUser'),

    path('userprofile', views.UserProfile, name='UserProfile'),


    path('registerAsVenue', views.registerAsVenue, name='registerAsVenue'),    
    path('venueRegistrationSubmitted', views.venueRegistrationSubmitted, name='venueRegistrationSubmitted'),   

    path('logout', views.logoutUser, name="logout"),
    path("success", views.success, name="success"),

]



