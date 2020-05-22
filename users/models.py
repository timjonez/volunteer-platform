from django.db import models
from address.models import AddressField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager



# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    phone_number = PhoneNumberField()
    church_name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True)
    #denomination = models.CharField(max_length=200)
    address = AddressField(on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['church_name', 'phone_number','address']

    objects = CustomUserManager()

    def __str__(self):
        return self.church_name
