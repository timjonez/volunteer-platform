from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email',)
    list_filter = ('is_active','date_joined',)
    fieldsets = (
        (None, {'fields': ('email','church_name', 'address', 'phone_number', 'description', 'password', 'date_joined')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('church_name','address', 'phone_number', 'email', 'password1', 'password2', 'is_active')}
        ),
    )
    search_fields = ('church_name',)
    ordering = ('church_name',)


admin.site.register(CustomUser, CustomUserAdmin)
