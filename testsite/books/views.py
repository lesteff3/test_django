from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import BooksForm

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