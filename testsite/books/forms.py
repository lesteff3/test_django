from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Books
from django.forms import ModelForm, TextInput, NumberInput, Select
from django import forms







class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author', 'count', 'price']


        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название книги'
            }),
            'author': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Автор книги'
            }),
            'count': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'кол-во книг'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'цена'
            }),

        }
#