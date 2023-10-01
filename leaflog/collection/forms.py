from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Location


class CollectionAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'uk-input', 'placeholder': 'Username' })
        self.fields['password'].widget.attrs.update({'class': 'uk-input', 'placeholder': 'Password' })


class LocationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'uk-input'})
        self.fields['description'].widget.attrs.update({'class': 'uk-textarea'})

    class Meta:
        model = Location
        fields = ['name', 'description']
