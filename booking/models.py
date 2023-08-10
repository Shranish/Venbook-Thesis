from django.conf import settings
from django.db import models

from events.models import VenbookEventInfo, VenbookEventRequest

# Create your models here.
class AdvancePaymentReceived_Log(models.Model):
    pm = (
    ('Esewa', 'Esewa'),
    ('Khalti', 'Khalti' ),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    booking_request = models.ForeignKey(VenbookEventRequest, on_delete=models.CASCADE)
    method = models.CharField(max_length=150, choices=pm)
    amount = models.FloatField()
    transaction_date =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.booking_request} - {self.transaction_date}"

class AdvancePaymentSent_Log(models.Model):
    pm = (
    ('Esewa', 'Esewa'),
    ('Khalti', 'Khalti' ),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    booking_request = models.ForeignKey(VenbookEventRequest, on_delete=models.CASCADE)
    method = models.CharField(max_length=150, choices=pm)
    amount = models.FloatField()
    transaction_date =  models.DateTimeField(auto_now_add=True)