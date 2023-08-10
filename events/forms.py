from django import forms

from events.models import EventType, OutEventInfo, VenbookEventInfo
from accounts.models import VenueAccount

class OutEventInfoForm(forms.ModelForm):
    venue_account = forms.ModelChoiceField(queryset=VenueAccount.objects.all(),
                                widget=forms.Select(
                                        attrs={'class':'form-control'}))
    event_name = forms.CharField(max_length=155,
                            widget= forms.TextInput(
                                attrs={'class':'form-control'}))
    event_date = forms.DateField(widget= forms.DateInput(
                                attrs={'type': 'date', 'class':'form-control'}))

    event_type = forms.ModelChoiceField(queryset=EventType.objects.all(),
                                widget=forms.Select(
                                        attrs={'class':'form-control'}))
    people = forms.CharField(max_length=155,
                            widget= forms.TextInput(
                                attrs={'class':'form-control'}))
    event_details = forms.CharField(max_length=355,
                                widget= forms.Textarea(
                                    attrs={'class':'form-control textArea'}))
    

    class Meta:
        model = OutEventInfo
        fields=[ 
            "venue_account",
            "event_name",
            "event_date",
            "event_type",
            "people",
            "event_details",          
        ]


class OutEventsUserInfoForm(forms.ModelForm):

    first_name = forms.CharField(max_length=155,
                            widget= forms.TextInput(
                                attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=155,
                            widget= forms.TextInput(
                                attrs={'class':'form-control'}))
    email = forms.EmailField(widget= forms.EmailInput(
                                attrs={'class':'form-control'}))
    phone = forms.CharField(max_length=10,
                                widget= forms.TextInput(
                                    attrs={'class':'form-control'}))
    

    class Meta:
        model = OutEventInfo
        fields=[
            "first_name",
            "last_name",
            "email",
            "phone",          
        ]


class VenbookEventInfoForm(forms.ModelForm):
    venue_account = forms.ModelChoiceField(queryset=VenueAccount.objects.all(),
                                widget=forms.Select(
                                        attrs={'class':'form-control'}))
    full_name = forms.CharField(max_length=155,
                            widget= forms.TextInput(
                                attrs={'class':'form-control'}))
    address = forms.CharField(max_length=155,
                            widget= forms.TextInput(
                                attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=155,
                            widget= forms.EmailInput(
                                attrs={'class':'form-control'}))
    phone = forms.CharField(max_length=10,
                                widget= forms.TextInput(
                                    attrs={'class':'form-control'}))
    event_name = forms.CharField(max_length=155,
                            widget= forms.TextInput(
                                attrs={'class':'form-control'}))
    event_date = forms.DateField(widget= forms.DateInput(
                                attrs={'type': 'date', 'class':'form-control'}))

    event_type = forms.ModelChoiceField(queryset=EventType.objects.all(),
                                widget=forms.Select(
                                        attrs={'class':'form-control'}))
    people = forms.CharField(max_length=155,
                            widget= forms.TextInput(
                                attrs={'class':'form-control'}))
    event_details = forms.CharField(max_length=355,
                                widget= forms.Textarea(
                                    attrs={'class':'form-control detail-e'}))
    

    class Meta:
        model = VenbookEventInfo
        fields=[ 
            'venue_account',
            'full_name',
            'address',
            'email',
            'phone',
            "event_name",
            "event_date",
            "event_type",
            "people",
            "event_details",          
        ]