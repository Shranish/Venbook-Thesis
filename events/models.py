from django.conf import settings
from django.db import models

from accounts.models import VenueAccount

# Create your models here.
class EventType(models.Model):
    name=models.CharField(max_length=155)

    def __str__(self):
        return self.name

class OutEventInfo(models.Model):
    venue_account = models.ForeignKey(VenueAccount, on_delete=models.CASCADE) 
    event_name = models.CharField(max_length=155)
    event_date = models.DateField(max_length=155)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    people = models.CharField(max_length=155)
    event_details = models.TextField()
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event_name} - {self.event_date}"
    

    def get_event_of_venue(venue_account):
        return OutEventInfo.objects.filter(venue_account=venue_account)
    



class OutEventsUserInfo(models.Model):
    event_info = models.ForeignKey(OutEventInfo, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    email = models.EmailField()
    phone= models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} - {self.event_info}"


class VenbookEventInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=155)
    address = models.CharField(max_length=155)
    email = models.EmailField(max_length=155)
    phone = models.CharField(max_length=10)
    venue_account = models.ForeignKey(VenueAccount, on_delete=models.CASCADE) 
    event_name = models.CharField(max_length=155)
    event_date = models.DateField(max_length=155)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    people = models.CharField(max_length=155)
    event_details = models.TextField()
    registered_at = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return f"{self.event_name} - {self.event_date}"

    


class VenbookEventRequest(models.Model):
    venue_event_info = models.ForeignKey(VenbookEventInfo, on_delete=models.CASCADE)
    accept = models.BooleanField(default=False, blank=True, null=True)
    reject = models.BooleanField(default=False, blank=True, null=True)
    reject_reason = models.TextField(null=True,blank=True)
    advance_quotation = models.IntegerField(blank=True, null=True)
    cancelled = models.BooleanField(default=False, blank=True, null=True)
    advance_payment_received = models.BooleanField(default=False, blank=True, null=True)
    advance_payment_sent = models.BooleanField(default=False, blank=True, null=True)

   

    def __str__(self):
        return f"{self.venue_event_info.venue_account} - {self.venue_event_info} - {self.accept} - {self.reject}"

    def count_booked_event(request):
        venue_id = VenueAccount.get_venue_account_instance(request.user)[0].id
        venue_instance = VenueAccount.objects.get(id=venue_id)
        count = VenbookEventRequest.objects.filter(venue_event_info__venue_account = venue_instance, accept=True, reject=False, cancelled = False).count()

        count2 = OutEventsUserInfo.objects.filter(event_info__venue_account = venue_instance).count()

        return count+ count2

    def count_event_request(request):
        venue_id = VenueAccount.get_venue_account_instance(request.user)[0].id
        venue_instance = VenueAccount.objects.get(id=venue_id)
        count = VenbookEventRequest.objects.filter(venue_event_info__venue_account = venue_instance, accept=False, reject=False).count()

        return count
        
    def count_declined_request(request):
        venue_id = VenueAccount.get_venue_account_instance(request.user)[0].id
        venue_instance = VenueAccount.objects.get(id=venue_id)
        count = VenbookEventRequest.objects.filter(venue_event_info__venue_account = venue_instance, accept=False, reject=True).count()

        return count
