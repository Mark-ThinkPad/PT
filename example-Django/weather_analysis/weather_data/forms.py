from django import forms


class RegionForm(forms.Form):
    latitude = forms.FloatField()
    longitude = forms.FloatField()
    is_display = forms.BooleanField(required=False)
