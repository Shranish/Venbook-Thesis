from django.dispatch import receiver

from django.core.mail import send_mail
from django.conf import settings

from accounts.models import is_verified
from django.db.models.signals import post_save


@receiver(post_save, sender=is_verified)
def send_email(sender, instance, created, **kwargs):
  if instance.verified == True and  instance.unverified == False:
    send_mail(
     subject='Venbook Venue Verification',
     message=f'Hello {instance.user.first_name}, The venue you registered with the name {instance.venue_account} has been verified. Please visit venbook to check venue dashboard',
     from_email=settings.EMAIL_HOST_USER,
     recipient_list=[instance.user.email]
     )
  elif instance.unverified == True and instance.verified == False:
    send_mail(
     subject='Venbook Venue Verification',
     message=f'Hello {instance.user.first_name}, The venue you registered with the name {instance.venue_account} could not be verified due to the following reasons: \n {instance.unverified_msg}',
     from_email=settings.EMAIL_HOST_USER,
     recipient_list=[instance.user.email]
     )