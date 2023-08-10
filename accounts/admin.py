from django.contrib import admin
from accounts.models import Account, UpdateSubscription, VenueAccount, VenueImages, is_verified
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Accounts'

class CustomizedUserAdmin (UserAdmin):
    inlines = (AccountInline, )

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin )

admin.site.register(UpdateSubscription)
admin.site.register(VenueAccount)
admin.site.register(VenueImages)
admin.site.register(is_verified)
