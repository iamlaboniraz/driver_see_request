from django import forms
from .models import requestModel

class requestForm(forms.ModelForm):
    class Meta:
        model= requestModel
        fields = ['name']