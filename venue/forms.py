from cgitb import text
from django import forms
from venue.models import VenuePricing

class pricing(forms.ModelForm):
    min_people = forms.IntegerField(
                    widget= forms.NumberInput(attrs={'min': '0','placeholder': '0','class':'priceInput'}))
    mid_people = forms.IntegerField(
                    widget= forms.NumberInput(attrs={'min': '0','placeholder': '0','class':'priceInput'}))
    max_people = forms.IntegerField(
                    widget= forms.NumberInput(attrs={'min': '0','placeholder': '0','class':'priceInput'}))
    dj_price = forms.IntegerField(
                    widget= forms.NumberInput(attrs={'min': '0','placeholder': '0','class':'priceInput'}))
    decoration = forms.BooleanField(
                    widget= forms.CheckboxInput(attrs={'class':'priceInput'}))        
    projectors = forms.IntegerField(
                    widget= forms.NumberInput(attrs={'min': '0','placeholder': '0','class':'priceInput'}))
    class Meta:
        model = VenuePricing
        fields=[
            "venue_account",
            "min_people",
            "mid_people",
            "max_people",
            "dj_price",
            "decoration",
            "projectors",
    ]





