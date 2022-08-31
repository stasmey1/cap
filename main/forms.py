from .models import *
from django import forms

class CapitalSelectForm(forms.Form):
    capital = forms.BooleanField()


class GroupSelectForm(forms.Form):
    group = forms.BooleanField()


class AddCountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name', 'capital', 'сontinent', 'group', 'info', 'img_country', 'flag']
        order_dy = ['name']

class SearchForm(forms.Form):
    search_input = forms.CharField(label='')
