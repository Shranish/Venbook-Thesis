from django.contrib import admin

from booking.models import AdvancePaymentReceived_Log, AdvancePaymentSent_Log

# Register your models here.
admin.site.register(AdvancePaymentReceived_Log)
admin.site.register(AdvancePaymentSent_Log)