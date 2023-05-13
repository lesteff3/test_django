from django.db.models import F
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from .forms import *
from .models import *



def index(request):
    public = Books.objects.filter(is_published=True)
    for i in public:
        if i.count <= 0:
            i.is_published = False
            i.save()

    return render(request, 'books/index.html', { 'public' : public})


def stats(request):
    author = Author.objects.all()
    books = Books.objects.filter(count__gt=0).filter(stock__gt=0).annotate(sell_book=F('stock') / F('count'))
    total_books= 0
    for book in Books.objects.values_list('count', flat=True):
        total_books += book

    total_sold_books = 0

    for c in Books.objects.values_list('stock', flat=True):
        total_sold_books += c
    # Author.objects.filter(id=1).values('bookss__count')
    get_all_book_author = Author.objects.values_list('bookss__count', flat=True)


    return render(request, 'books/stats.html', {
        'total_books': total_books,
        'total_sold_books': total_sold_books,
        'books': books,
        'get_all_book_author': get_all_book_author,
        'author': author,

    })


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




class BookDetailView(View):
    def get(self,request, pk):
        book = Books.objects.get(id=pk)
        book.count = book.count - 1
        book.stock = book.stock + 1

        book.save()


        return render(request, 'books/details_view.html', {'book':book})