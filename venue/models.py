from operator import mod
from unicodedata import name
from django.conf import settings
from django.db import models
from django.forms import ModelForm, TextInput
from accounts.models import VenueAccount

from multiselectfield import MultiSelectField

# Create your models here.
class VenuePricing(models.Model):
    venue_account = models.ForeignKey(VenueAccount, on_delete=models.CASCADE,null=True,blank=True)
    min_people = models.IntegerField(null=True,blank=True)
    mid_people = models.IntegerField(null=True,blank=True)
    max_people = models.IntegerField(null=True,blank=True)
    # Additional Charges
    dj_price = models.IntegerField(null=True,blank=True)
    decoration = models.BooleanField(default=False,null=True,blank=True)
    projectors = models.IntegerField(null=True,blank=True)
    

    def __str__(self):
        return self.venue_account.name

    def get_venue_pricing(venue_id):
        return VenuePricing.objects.filter(venue_account = venue_id)[0]

class VenueFacilitiesServices(models.Model):
    venue_choices = (
    ('DJ Service', 'DJ Service'),
    ('Parking Space', 'Parking Space' ),
    ('Customized decoration', 'Customized decoration'),
    ('Projectors', 'Projectors'),
    ('Changing Room', 'Changing Room'),
    ('Makeup Service', 'Makeup Service'),
    ('Fireworks', 'Fireworks'),
    ('Live Music', 'Live Music'),)
    venue_account = models.ForeignKey(VenueAccount, on_delete=models.CASCADE,null=True,blank=True)
    choice =MultiSelectField(choices=venue_choices)


class VenueReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    venue_account = models.ForeignKey(VenueAccount, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment