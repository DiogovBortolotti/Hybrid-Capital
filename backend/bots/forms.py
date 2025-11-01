from django import forms
from .models import ChaveAPI

class ChaveAPIForm(forms.ModelForm):
    api_secret = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = ChaveAPI
        fields = ['nome', 'api_key', 'api_secret', 'testnet']
