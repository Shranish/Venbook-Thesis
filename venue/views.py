from multiprocessing import context
from xml.dom.expatbuilder import Rejecter
from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render

from accounts.models import VenueAccount
from booking.views import is_ajax
from events.forms import OutEventInfoForm, OutEventsUserInfoForm, VenbookEventInfoForm
from events.models import OutEventInfo, OutEventsUserInfo, VenbookEventInfo, VenbookEventRequest
from venue.forms import pricing
from venue.models import VenueFacilitiesServices, VenuePricing, VenueReview
from django.contrib import messages

import datetime

from django.core.mail import send_mail

# Create your views here.


def PriceExistStatus(id):
    price_exist_status = False

    if VenuePricing.objects.filter(venue_account=id).exists():
        price_exist_status = True
    else:
        price_exist_status = False

    return price_exist_status


def VenuePriceData(id):
    venueData = None
    if VenuePricing.objects.filter(venue_account=id).exists():
        venueData = VenuePricing.objects.get(venue_account=id)
    return venueData


def VenueEdit(request, id):
    weekagodate = datetime.date.today() + datetime.timedelta(days=7)
    venue_id = VenueAccount.get_venue_account_instance(request.user)[0]
    venue_instance = VenueAccount.objects.get(id=id)

    eventupcoming=[]
    # for upcoming events
    for i in VenbookEventRequest.objects.filter(venue_event_info__venue_account = venue_instance, accept=True, reject=False, cancelled = False):
        if i.venue_event_info.event_date > datetime.date.today() and i.venue_event_info.event_date < weekagodate:
            eventupcoming.append(i)

    if id == venue_id.id:
        form = pricing()
        data = {'venue_account': id}
        eventForm = OutEventInfoForm(initial=data)
        eventUserForm = OutEventsUserInfoForm(initial=data)

        venue_instance = VenueAccount.objects.get(id=id)

        if ('addnewpriceBtn' in request.POST):
            form = pricing(request.POST)
            if form.is_valid():
                f = form.save()
                f.venue_account = venue_instance
                f.save()

        elif ('createeventBtn' in request.POST):
            eventForm = OutEventInfoForm(request.POST)
            eventUserForm = OutEventsUserInfoForm(request.POST)
            if eventForm.is_valid() and eventUserForm.is_valid():
                a = eventForm.save()
                a.save()

                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                email = request.POST.get('email')
                phone = request.POST.get('phone')

                OutEventsUserInfoData = OutEventsUserInfo.objects.create(
                    event_info=a, first_name=first_name, last_name=last_name, email=email, phone=phone)
                OutEventsUserInfoData.save()

                return redirect('venue:VenueEdit', id=id)

            else:
                return render(request, 'venue/editvenue.html',
                    {
                        'venue_instance': venue_instance,
                        'price_exist_status': PriceExistStatus(id),
                        'VenuePriceData':VenuePriceData(id),
                        'form':form,
                        'eventForm':eventForm,
                        'eventUserForm':eventUserForm,
                        'eventupcoming': len(eventupcoming),
                        'outevent_exists':outevent_exists,
                        'outvenbookEvent_list':outvenbookEvent_list,

                        'bookedEventCount':VenbookEventRequest.count_booked_event(request),
                        'RequestEventCount':VenbookEventRequest.count_event_request(request),
                        'DeclinedRequestEventCount':VenbookEventRequest.count_declined_request(request),
                    })

        event_exists = False
        if VenbookEventRequest.objects.filter(venue_event_info__venue_account=venue_instance, accept=True, reject=False, cancelled = False).exists():
            event_exists = True
            venbookEvent_list = []

            venbooklist = VenbookEventRequest.objects.filter(
                venue_event_info__venue_account=venue_instance, accept=True, reject=False, cancelled = False).order_by('-venue_event_info__registered_at')

            for i in venbooklist:
                venbookEvent_list.append(i)

        else:
            venbookEvent_list = []
            event_exists = False

        outevent_exists = False
        if OutEventsUserInfo.objects.filter(event_info__venue_account = venue_instance).exists():
            outevent_exists = True
            outvenbookEvent_list = []

            outvenbooklist = OutEventsUserInfo.objects.filter(event_info__venue_account = venue_instance).order_by('-event_info__registered_at')

            for i in outvenbooklist:
                outvenbookEvent_list.append(i)

        else:
            outvenbookEvent_list =[]
            outevent_exists = False
                              
        context ={
            'venue_instance':venue_instance,
            'price_exist_status': PriceExistStatus(id),
            'VenuePriceData':VenuePriceData(id),
            'form':form,
            'eventForm':eventForm,
            'eventUserForm':eventUserForm,
            'outevent_exists':outevent_exists,
            'outvenbookEvent_list':outvenbookEvent_list,
            'event_exists':event_exists,
            'venbookEvent_list':venbookEvent_list,
            'eventupcoming': len(eventupcoming),

            'bookedEventCount':VenbookEventRequest.count_booked_event(request),
            'RequestEventCount':VenbookEventRequest.count_event_request(request),
            'DeclinedRequestEventCount':VenbookEventRequest.count_declined_request(request),
            }

        return render(request, 'venue/editvenue.html', context)
    else:
        raise Http404


def VenuePriceUpdate(request):
    if request.method == "POST" and 'updatenewprice':
        venue_id = request.POST.get('venue_id')
        min_people = request.POST.get('min-people')
        mid_people = request.POST.get('mid-people')
        max_people = request.POST.get('max-people')
        dj_price = request.POST.get('dj_price')
        decoration = request.POST.get('decoration')
        projectors = request.POST.get('projectors')

        venue_price_instance = VenuePricing.objects.get(venue_account=venue_id)
        venue_price_instance.min_people = min_people
        venue_price_instance.mid_people = mid_people
        venue_price_instance.max_people = max_people

        if decoration == "on":
            venue_price_instance.decoration = True
        else:
            venue_price_instance.decoration = False

        venue_price_instance.dj_price = dj_price
        venue_price_instance.projectors = projectors
        venue_price_instance.save()

    return redirect('venue:VenueEdit', id=venue_id)


def VenueDescUpdate(request, id):
    if request.method == "POST" and 'updatedesc':
        venue_acc_instance = VenueAccount.objects.get(user=request.user)

        venue_desc = request.POST.get('venue_description')
        venue_acc_instance.description = venue_desc
        venue_acc_instance.save()
    return redirect('venue:VenueEdit', id=id)


def VenueDetail(request, id):
# Send email to customer
    def send_booking_request_email(email, name, eventname, date):
        send_mail(
            subject='Venbook Event Booking Request',
            message=f'Hello {name}, The event booking request for {eventname} on {date} has been sent to venue for confirmation. You shall be notified regarding the confirmation status of your request through email. Thank you!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )

# Send email to venue
    def send_booking_request_email_to_venue(email, vname, name, eventname, date):
        send_mail(
            subject='Venbook Event Booking Request',
            message=f'Hello {vname}, You have received a new event booking request from {name} with event name {eventname} on {date}. Please update the request status through Booking Request Page. The status shall be informed to respective customer. Thank you!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )
    venue_instance = VenueAccount.objects.get(id=id)
    venue_services = None
    venue_price = None

    reviews = VenueReview.objects.filter(venue_account=venue_instance)

    if VenuePricing.objects.filter(venue_account=venue_instance).exists():
        venue_price = VenuePricing.objects.filter(
            venue_account=venue_instance)[0]

    if VenueFacilitiesServices.objects.filter(venue_account=venue_instance).exists():
        venue_services = VenueFacilitiesServices.objects.filter(
            venue_account=venue_instance)[0]

    if request.user.is_authenticated:
        data = {'venue_account': id,
                'full_name': request.user.first_name + " " + request.user.last_name,
                'email': request.user.email}
    else:
        data = {'venue_account': " ",
                'full_name': " ",
                'email': " "}
    EventBookForm = VenbookEventInfoForm(initial=data)

    # For calender Events
    allevents = []

    outevents = OutEventInfo.get_event_of_venue(venue_instance)
    venbookevents = VenbookEventRequest.objects.filter(venue_event_info__venue_account=venue_instance, accept=True, reject=False, cancelled = False)
    for i in outevents:
        allevents.append(i)

    for i in venbookevents:
        allevents.append(i)

    if (request.method == "POST"):
        EventBookForm = VenbookEventInfoForm(request.POST)

        if EventBookForm.is_valid():
            print("form Valid")
            e = EventBookForm.save()
            e.user = request.user
            e.save()
            print("form saved")

            # saves the booking detail to booking request which is to be sent to the venue
            f = VenbookEventRequest.objects.create(venue_event_info=e)
            f.save()

            send_booking_request_email(
                e.email, e.full_name, e.event_name, e.event_date)
            send_booking_request_email_to_venue(
                venue_instance.user.email, venue_instance.user, e.full_name, e.event_name, e.event_date)

            return redirect('venue:VenueDetail', id=id)

        else:
            return render(request, 'venue/venue-detail.html',
            {
                'venue_instance': venue_instance,
                'venue_price': venue_price,
                'EventBookForm': EventBookForm,
                'allevents': allevents,
                'venue_services': venue_services,
                'reviews':reviews
            })

    context = {
        'venue_instance': venue_instance,
        'venue_price': venue_price,
        'EventBookForm': EventBookForm,
        'allevents': allevents,
        'venue_services': venue_services,
        'reviews':reviews
    }
    return render(request, 'venue/venue-detail.html', context)


def VenueDisplay(request):
    return render(request, 'venue/displaypage.html')


def BookingRequest(request):
    venue_id = VenueAccount.get_venue_account_instance(request.user)[0]
    requests = VenbookEventRequest.objects.filter(
        venue_event_info__venue_account=venue_id)
    context = {
        'requests': requests
    }
    return render(request, 'venue/booking-request.html', context)

def AddReview(request):
    if is_ajax(request=request):
        print("here in add review")
        venue_id = request.POST.get('venue_id') # getting data from first_name input 
        comment = request.POST.get('comment')  # getting data from last_name input
        venue_instance = VenueAccount.objects.get(id = venue_id)
        f = VenueReview.objects.create(user = request.user, venue_account = venue_instance, comment = comment)
        f.save()

        return JsonResponse("Comment Added", safe=False)

