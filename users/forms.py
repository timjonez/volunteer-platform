from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from address.models import AddressField
from phonenumber_field.formfields import PhoneNumberField

from .models import CustomUser
from django.db import models
from django import forms


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        address = AddressField()
        model = CustomUser
        fields = ('church_name','address', 'phone_number', 'email', 'password1', 'password2','is_staff')



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class ContactForm(forms.Form):
    user = forms.CharField(required=True, label='Your Name' )
    email = forms.EmailField(required=True, label='Email')
    phone = PhoneNumberField()
    message = forms.CharField(widget=forms.Textarea, required=True, max_length=1000)
