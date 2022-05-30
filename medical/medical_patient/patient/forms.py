from django import forms
from .models import Patient


class PatientForm(forms.Form):
    last_name = forms.CharField(),
    first_name = forms.CharField(),
    second_name = forms.CharField(),
    age = forms.IntegerField(),
    date_of_birth = forms.DateField(),
    address = forms.CharField(),
    diagnosis = forms.TextInput(),
    is_agree = forms.BooleanField(),
