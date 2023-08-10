from django.contrib import admin

from venue.models import VenueFacilitiesServices, VenuePricing, VenueReview

# Register your models here.
admin.site.register(VenuePricing)
admin.site.register(VenueFacilitiesServices)
admin.site.register(VenueReview)