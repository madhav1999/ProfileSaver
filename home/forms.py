from logging import NOTSET
from socket import fromshare
from django import forms
from django.core.exceptions import ValidationError

from .models import details


class forYouForm(forms.ModelForm):
    class Meta:
        model = details
        fields = ["FirstName", "LastName", "DateofBirth",
                  "State", "Country", "Education", "Password", "Occupation", "gender", "EmailName"]
        widgets = {
            'Password': forms.PasswordInput(),
            'DateofBirth': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }),
        }
