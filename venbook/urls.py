"""venbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls import include

from django.contrib.auth import views as auth_views

from booking import views as bookingView
from accounts import views as accountsView
from venue import views as venueView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('home.urls')),
    path('accounts/',include('accounts.urls')),
    path('social_login/', include('allauth.urls')),
    path('venue/',include('venue.urls')),
    path('events/',include('events.urls')),
    path('calender/',include('calender.urls')),
    path('bookings/',include('booking.urls')),

    path('SendRequestUpdate/',bookingView.SendRequestUpdate,name="SendRequestUpdate"),
    path('Cancelbooking/',bookingView.Cancelbooking,name="Cancelbooking"),

    path('AddReview/',venueView.AddReview,name="AddReview"),


    path("EsewaRequestView/", bookingView.EsewaRequestView, name="EsewaRequestView"),


    path("AddUserInfo/", accountsView.AddUserInfo, name="AddUserInfo"),
    path("UpdateUserInfo/", accountsView.UpdateUserInfo, name="UpdateUserInfo"),


    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
        name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
        name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
        name="password_reset_complete"),


    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
