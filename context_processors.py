from accounts.models import is_verified,VenueAccount

def venue_verification_status(request):
    if request.user.is_authenticated:
        venue_reg = False
        status = False
        venue_id = None
        status2 = False

        if VenueAccount.objects.filter(user=request.user).exists():
            venue_reg = True
            user_venue_instance = is_verified.objects.filter(user = request.user)[0]
            status = user_venue_instance.verified
            status2 = user_venue_instance.unverified
            venue_id = VenueAccount.objects.get(user = request.user).id
        
    else:
        venue_reg = False
        status = False
        status2 = False
        venue_id = None
    return {'status':status, 'venue_reg':venue_reg,'venue_id':venue_id,'status2':status2}