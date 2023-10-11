from django.forms import ModelForm
from django.forms.widgets import HiddenInput, DateInput
from django.contrib.auth.forms import AuthenticationForm

from .models import Location, Taxon, Accession


class CollectionAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'uk-input', 'placeholder': 'Username' })
        self.fields['password'].widget.attrs.update({'class': 'uk-input', 'placeholder': 'Password' })


class LocationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'uk-input'})
        self.fields['description'].widget.attrs.update({'class': 'uk-textarea'})

    class Meta:
        model = Location
        fields = ['name', 'description']


class TaxonForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'uk-input'})
        self.fields['rank'].widget.attrs.update({'class': 'uk-input'})
        self.fields['parent'].widget.attrs.update({'data-id': 'parent'})

    class Meta:
        model = Taxon
        fields = ['parent', 'rank', 'name']
        widgets = {
            'parent': HiddenInput,
        }


class AccessionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['accnum'].widget.attrs.update({'class': 'uk-input', 'autocomplete': 'off'})
        self.fields['location'].widget.attrs.update({'class': 'uk-input'})
        self.fields['taxon'].widget.attrs.update({'data-id': 'taxon'})
        self.fields['status'].widget.attrs.update({'class': 'uk-input'})
        self.fields['material'].widget.attrs.update({'class': 'uk-input'})
        self.fields['source'].widget.attrs.update({'class': 'uk-input'})
        self.fields['collected'].widget.attrs.update({'class': 'uk-input'})
        self.fields['description'].widget.attrs.update({'class': 'uk-textarea'})

    class Meta:
        model = Accession
        fields = ['accnum', 'taxon', 'location', 'status', 'material', 'source', 'collected', 'description']
        widgets = {
            'taxon': HiddenInput,
            'collected': DateInput,
        }
