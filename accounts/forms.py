from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import VenueAccount

from accounts.models import VenueImages
from events.models import EventType

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class venueRegistrationForm(forms.ModelForm):
    name = forms.CharField(max_length=155,
                            widget= forms.TextInput(
                                attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=155,
                            widget= forms.TextInput(
                                attrs={'class':'form-control'}))
    pan = forms.CharField(max_length=155,
                            widget= forms.TextInput(
                                attrs={'class':'form-control'}))
    city = forms.CharField(max_length=155,
                            widget= forms.TextInput(
                                attrs={'class':'form-control'}))
    address = forms.CharField(max_length=155,
                            widget= forms.TextInput(
                                attrs={'class':'form-control'}))
    phone = forms.CharField(max_length=155,
                            widget= forms.TextInput(
                                attrs={'class':'form-control'}))

    event_types = forms.ModelChoiceField(queryset=EventType.objects.all(),
                                widget=forms.Select(
                                        attrs={'class':'form-control'}))

    description = forms.CharField(max_length=355,
                                widget= forms.Textarea(
                                    attrs={'class':'form-control'}))
    capacity = forms.CharField(max_length=155,
                                widget= forms.TextInput(
                                    attrs={'class':'form-control'}))

    class Meta:
        model = VenueAccount
        fields=[
            "name",
            "email",
            "pan",
            "city",
            "address",
            "phone",
            "event_types",
            "description",
            "capacity",
            "owner_citizenship",
            "venue_pp",           
        ]

class VenueImagesForm(forms.ModelForm):
    image=forms.ImageField(
        label=""
    )

    class Meta:
        model=VenueImages
        fields = ("image",)
