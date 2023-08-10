from email.policy import default
import json
from django.shortcuts import render

from events.models import OutEventInfo, VenbookEventInfo, VenbookEventRequest
from accounts.models import VenueAccount
from django.core import serializers



# Create your views here.

def viewCalender(request):
    venue_instance = VenueAccount.get_venue_account_instance(request.user)[0]
    allevents= []
    outevents = OutEventInfo.get_event_of_venue(venue_instance)
    venbookevents = VenbookEventRequest.objects.filter(venue_event_info__venue_account = venue_instance, accept = True, reject = False, cancelled =False)
    
    for i in outevents:
        allevents.append(i)
        
    for i in venbookevents:
        allevents.append(i)
    
    context={
        'venue_instance':venue_instance,
        'allevents':allevents
    }
    return render(request, 'calender/calender.html',context)

