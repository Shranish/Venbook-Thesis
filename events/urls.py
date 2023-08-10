from django.urls import path

from . import views

app_name='events'

urlpatterns= [
    path('create-new-event', views.CreateNewEvent, name='CreateNewEvent'),

]


