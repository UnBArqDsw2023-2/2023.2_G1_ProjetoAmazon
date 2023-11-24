from django import forms
from django.contrib.auth.forms import UserCreationForm

from authuser.models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['email', 'name']
