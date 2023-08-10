import datetime
from multiprocessing import context
from django.conf import settings

import requests as req

from django.http import JsonResponse
from django.shortcuts import redirect, render
from booking.models import AdvancePaymentReceived_Log

from events.models import VenbookEventInfo, VenbookEventRequest
from django.shortcuts import HttpResponse

from django.core.mail import send_mail

import xml.etree.ElementTree as ET

# Create your views here.
def Mybookings(request):
    # my booking page view here
    today = datetime.date.today()
    bookingHistory = VenbookEventRequest.objects.filter(venue_event_info__user = request.user, cancelled = False)
    context={
        'bookingHistory': bookingHistory,
        'today':today
    }
    return render(request, 'booking/mybooking.html',context)

def Cancelbooking(request):
    def send_canceled_status_to_customer(email,vname, name, eventname, date):
        send_mail(
            subject='Venbook Event Booking Canceled',
            message=f'Hello {name}, Your event booking in {vname} with event name {eventname} for {date} has been canceled. Please check Canceled Booking Page for further details. Thank you!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )
    def send_canceled_status_to_venue(email,vname, name, eventname, date):
        send_mail(
            subject='Venbook Event Booking Canceled',
            message=f'Hello {vname}, {name} has canceled the booking with event name {eventname} for {date}. Thank you!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )


    if is_ajax(request=request):
        print("in cancel booking")
        id = request.POST.get('id') # getting data from first_name input 
        remainingDays = request.POST.get('remainingDays')  # getting data from last_name input

        requestToCancel = VenbookEventRequest.objects.get(id = id)
        requestToCancel.cancelled = True
        requestToCancel.save()

        send_canceled_status_to_customer(requestToCancel.venue_event_info.email, requestToCancel.venue_event_info.venue_account, requestToCancel.venue_event_info.full_name, requestToCancel.venue_event_info.event_name, requestToCancel.venue_event_info.event_date)
        send_canceled_status_to_venue(requestToCancel.venue_event_info.venue_account.user.email, requestToCancel.venue_event_info.venue_account, requestToCancel.venue_event_info.full_name, requestToCancel.venue_event_info.event_name, requestToCancel.venue_event_info.event_date)
    

        # canceledVenbookRequest.objects.create(eventRequest = requestToCancel, remainingDays = remainingDays).save()


        # requestToCancel.delete()
    
    return JsonResponse("Updated Event Request",safe=False)



def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def SendRequestUpdate(request):
    def send_accepted_status(email,vname, name, eventname, date):
        send_mail(
            subject='Venbook Event Booking Request Confirmation',
            message=f'Hello {name}, Your event booking request with event name {eventname} has been accepted by {vname} for {date}. Please check My Booking Page for further details. Thank you!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )
    def send_rejected_status(email,vname, name, eventname, date):
        send_mail(
            subject='Venbook Event Booking Request Confirmation',
            message=f'Hello {name}, Your event booking request with event name {eventname} has been declined by {vname} for {date}. Please check My Booking Page for rejection reason and further details. Thank you!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )

    if is_ajax(request=request):
        id = request.POST.get('id') # getting data from first_name input 
        status = request.POST.get('status')  # getting data from last_name input

        if status == "True":
            quotation = request.POST.get('quotation')
            updateReqIfAccepted = VenbookEventRequest.objects.get(id = id)
            updateReqIfAccepted.accept = True
            updateReqIfAccepted.advance_quotation = quotation
            updateReqIfAccepted.save()
            send_accepted_status(updateReqIfAccepted.venue_event_info.email, updateReqIfAccepted.venue_event_info.venue_account, updateReqIfAccepted.venue_event_info.full_name, updateReqIfAccepted.venue_event_info.event_name, updateReqIfAccepted.venue_event_info.event_date)
        else:
            reason = request.POST.get('reason')
            updateReqIfRejected = VenbookEventRequest.objects.get(id = id)
            updateReqIfRejected.reject = True
            updateReqIfRejected.reject_reason = reason
            updateReqIfRejected.save() 
            send_rejected_status(updateReqIfRejected.venue_event_info.email, updateReqIfRejected.venue_event_info.venue_account, updateReqIfRejected.venue_event_info.full_name, updateReqIfRejected.venue_event_info.event_name, updateReqIfRejected.venue_event_info.event_date)
        
        return JsonResponse("Updated Event Request",safe=False)

def EsewaRequestView(request):
    if is_ajax(request=request):
        id = request.POST.get('id') # getting data from first_name input 
        quotation = request.POST.get('quotation')  # getting data from last_name input

    
        return JsonResponse("Updated Event Request",safe=False)

def EsewaVerifyView(request):
    oid = request.GET.get('oid')
    amt = request.GET.get('amt')
    refId = request.GET.get('refId')

    url ="https://uat.esewa.com.np/epay/transrec"
    d = {
        'amt': amt,
        'scd': 'EPAYTEST',
        'rid': refId,
        'pid':oid,
    }

    print(type(amt))

    resp = req.post(url, d)
    root = ET.fromstring(resp.content)
    status = root[0].text.strip()

    if status == "Success":
        req_obj = VenbookEventRequest.objects.get(id = oid)
        req_obj.advance_payment_received = True
        req_obj.save()

        save_paymentReceivedLog = AdvancePaymentReceived_Log.objects.create(user = req_obj.venue_event_info.user, booking_request =  req_obj, method = "Esewa", amount = amt)
        save_paymentReceivedLog.save()

        return redirect('home:index')

    else:
        pass

    return redirect('home:index')