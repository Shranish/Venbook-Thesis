from django.urls import path

from . import views
# namespace
app_name='booking'

urlpatterns= [
    path('mybookings', views.Mybookings, name='Mybookings'),
    path("esewa-verify/", views.EsewaVerifyView, name="esewaverify"),
]


