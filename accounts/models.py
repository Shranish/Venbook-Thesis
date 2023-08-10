
from django import forms
from django.db import models
from django.contrib.auth. models import User
from django.conf import settings



# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True,blank=True)
    phone = models.CharField(max_length=10,null=True,blank=True)
    address = models.CharField(max_length=155,null=True,blank=True)
    gender = models.CharField(
        max_length=6,
        choices=[('Male','Male'),('Female','Female'),('Other','Other')],
        null=True,blank=True
        
    )

    def __str__(self):
        return self.user.email

class UpdateSubscription(models.Model):
     user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1, on_delete=models.CASCADE)
     status = models.BooleanField(default=False)

     def __str__(self):
        return self.user.username


class VenueAccount(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=155)
    email = models.EmailField(max_length=255)
    pan = models.CharField(max_length=155)
    city = models.CharField(default="Kathmandu", max_length=255)
    address = models.CharField(max_length=255)
    lat = models.FloatField(null=True,blank=True)
    lon = models.FloatField(null=True,blank=True)
    phone = models.CharField(max_length=10)
    event_types = models.ForeignKey(to='events.EventType',on_delete=models.CASCADE)
    description = models.TextField()
    capacity = models.CharField(max_length=155)
    owner_citizenship = models.ImageField(default='default.jpg', upload_to ='owner_citizenship')
    venue_pp = models.ImageField(default='default.jpg', upload_to ='venue_pp')    


    def __str__(self):
        return self.name

    
    def get_venue_account_instance(user_id):
        return VenueAccount.objects.filter(user = user_id)

class is_verified(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    venue_account = models.ForeignKey(VenueAccount, on_delete=models.CASCADE, null=True, blank=True)
    verified = models.BooleanField(default=False)
    unverified = models.BooleanField(default=False)
    unverified_msg = models.TextField(null=True,blank=True)


    def __str__(self):
        return f"{self.venue_account} -- {self.verified}"

class VenueImages(models.Model):
    venue_account = models.ForeignKey(VenueAccount, on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to ='venue_images')


    def __str__(self):
        return f"{self.venue_account}"