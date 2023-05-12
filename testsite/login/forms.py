from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, AbstractUser
from django.db import models

class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'phone_number', 'email', 'password1' )

