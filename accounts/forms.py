from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # Professional comment: Form used for registering new users with email
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

class CustomUserChangeForm(UserChangeForm):
    # Professional comment: Form used for administrative updates to user profiles
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')