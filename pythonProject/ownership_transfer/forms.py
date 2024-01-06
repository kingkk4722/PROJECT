# ownership_transfer/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Ownership

class RegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    mobile_number = forms.CharField(max_length=15)
    email = forms.EmailField()
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class OwnershipForm(forms.ModelForm):
    class Meta:
        model = Ownership
        fields = ['model','IMEI_Number','mobile_number', 'email']

    mobile_number = forms.CharField(max_length=15)
    email = forms.EmailField()

    def __str__(self):
        return f"{self.model} {self.IMEI_Number} {self.mobile_number} {self.email}"

class OwnershipTransferForm(forms.Form):
    new_owner_username = forms.CharField(label='New Owner Username', max_length=100)