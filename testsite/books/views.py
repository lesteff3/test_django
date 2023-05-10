from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView


from .forms import *
from .models import *


def index(request):
    posts = Books.objects.all()
    return render(request, 'books/index.html', {'posts': posts, 'title': "Список Книг"})


def stats(request):

    return render(request, 'books/stats.html', {'title': "Статистика"})


def create(request):
    error = ''
    if request.method == "POST":
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была не верной'

    form = BooksForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'books/create.html', data)


