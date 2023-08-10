from django.urls import path

from . import views

app_name='calender'

urlpatterns= [
    path('', views.viewCalender, name='viewCalender'),

]



