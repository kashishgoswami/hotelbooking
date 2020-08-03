
from django import forms
class RegistrationForm(forms.Form):

    f_name=forms.CharField(max_length=100)
    l_name=forms.CharField(max_length=100)
    email=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)
