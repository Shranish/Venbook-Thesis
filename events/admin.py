from django.contrib import admin

from events.models import EventType, OutEventInfo, OutEventsUserInfo, VenbookEventInfo, VenbookEventRequest

# Register your models here.
admin.site.register(EventType) 
admin.site.register(OutEventInfo) 
admin.site.register(VenbookEventInfo) 
admin.site.register(OutEventsUserInfo) 
admin.site.register(VenbookEventRequest) 

